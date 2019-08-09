# Parser (CU, EMART24, GS25, Ministop, SevenEleven) 버전을 전부 합쳐서 model 에 일괄 올리는 작업을 할 예정임.
#TODO: Parser 를 최종 완성하고 나서 적은 양의 페이지만 불러오도롱 세팅해놓았던것을 전체 페이지를 로드하게 하고 최종 확인 해보기!!

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bogo.settings')
import django
django.setup()
from parsed_data.models import Product
from parsed_data.models import Product2
from parsed_data.models import Product3
from parsed_data.models import Product4
from parsed_data.models import Product5
import platform

# Chrome 창을 띄우지 않고(headless 하게) driver 를 사용하기 위한 options 변수 선언 및 설정 그리고 driver 선언
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--disable-gpu")
driver = webdriver.Chrome('./chromedriver', options=options)
driver.implicitly_wait(3)

# CU Parser
def cu_parser():
    # CU 페이지에 driver를 접속시킵니다.
    driver.get('http://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N')
    # 전체 페이지 LOAD 하기 (Test단계에서는 첫 번째 페이지만 로드)
    while 1:
        try:
            driver.find_element_by_css_selector(
                '#contents > div.relCon > div.prodListWrap > div > div.prodListBtn-w > a').click()
            time.sleep(1)
        # ElementClickInterceptedException Exception 이 발생하면 1초 대기한다.
        except ElementClickInterceptedException:
            time.sleep(1)
        except StaleElementReferenceException:
            time.sleep(1)
        # NoSuchElementException 이 발생하면 더 이상 불러올 상품이 없다는 뜻이니 페이지 LOAD 를 중단한다.
        except NoSuchElementException:
            print("CU Parsing END")
            break

    # 순서대로 파싱하기위한 변수 선언
    num = 17
    col = 1
    prod_list = []
    while 1:
        prod_input = []
        try:
            print(str(int(num / 17) * 40 + col - 40) + "번째 상품")
            # 상품의 이름 및 가격 (line1: name, line2: price)
            prod_input.append(driver.find_element_by_css_selector(
                '#contents > div.relCon > div.prodListWrap > ul:nth-child(%s) > li:nth-child(%s) > p.prodName' % (
                    num, col)).text)
            prod_input.append(driver.find_element_by_css_selector(
                '#contents > div.relCon > div.prodListWrap > ul:nth-child(%s) > li:nth-child(%s) > p.prodPrice' % (
                    num, col)).text)
            prod_input.append(driver.find_element_by_css_selector(
                '#contents > div.relCon > div.prodListWrap > ul:nth-child(%s) > li:nth-child(%s) > div > a' % (
                    num, col)).find_element_by_tag_name('img').get_attribute('src'))
            prod_input.append(driver.find_element_by_css_selector(
                "#contents > div.relCon > div.prodListWrap > ul:nth-child(%s) > li:nth-child(%s) > ul > li" % (
                    num, col)).text)
            col += 1
            if col is 40:
                col = 1
                num += 17
            prod_input[1] = prod_input[1].replace(',', '')
            prod_input[1] = prod_input[1].replace('원', '')
        except NoSuchElementException:
            print("CU Append successfully done.")
            break
        prod_list.append(prod_input)
    return prod_list


def emart_parser():
    # Emart 페이지에 driver를 접속시킨다.
    driver.get('https://www.emart24.co.kr/product/eventProduct.asp')
    num = 1
    col = 0
    prod_list = []
    while 1:
        try:
            while num < 16:
                prod_input = []
                print("emart parsing")
                print(num)
                prod_input.append(driver.find_element_by_css_selector(
                    '#regForm > div.section > div.eventProduct > div.tabContArea > ul > li:nth-child(%s) > div > p.productDiv' % num).text)
                prod_input.append(driver.find_element_by_css_selector(
                    '#regForm > div.section > div.eventProduct > div.tabContArea > ul > li:nth-child(%s) > div > p.price' % num).text)
                try:
                    prod_input.append(driver.find_element_by_css_selector(
                        '#regForm > div.section > div.eventProduct > div.tabContArea > ul > li:nth-child(%s) > div > p.productImg' % num).find_element_by_tag_name(
                        'img').get_attribute('src'))
                except NoSuchElementException:
                    pass

                prod_input[1] = prod_input[1].replace(',', '')
                prod_input[1] = prod_input[1].replace(' 원', '')

                if '→' in prod_input[1]:
                    prod_input[1] = prod_input[1].replace('→ ', '')
                    prod_input[1] = prod_input[1].split(' ')[1]

                eventtype = driver.find_element_by_xpath(
                    '//*[@id="regForm"]/div[2]/div[3]/div[2]/ul/li[%s]/div/div/p/img' % num).get_attribute('alt')
                print(eventtype)
                if '2 + 1 뱃지' in eventtype:
                    eventtype = '2+1'
                elif 'SALE 뱃지' in eventtype:
                    eventtype = 'sale'
                elif 'X2 더블 뱃지' in eventtype:
                    eventtype = 'dum'
                elif '1 + 1 뱃지 이미지' in eventtype:
                    eventtype = '1+1'
                elif '3 + 1 뱃지' in eventtype:
                    eventtype = '3+1'
                else:
                    eventtype = 'error!'
                prod_input.append(eventtype)
                prod_list.append(prod_input)
                num += 1
                if num is 16:
                    col += 1
                    num = 1
                    driver.find_element_by_css_selector(
                        '#regForm > div.section > div.eventProduct > div.paging > a.next.bgNone').click()
        except NoSuchElementException:
            print("파싱종료")
            break
        except StaleElementReferenceException:
            time.sleep(0.5)
        except ElementClickInterceptedException:
            time.sleep(1)
    return prod_list


def gs25_parser():
    # GS25 페이지에 driver를 접속시킨다.
    driver.get('http://gs25.gsretail.com/gscvs/ko/products/event-goods')
    driver.find_element_by_xpath('//*[@id="TOTAL"]').click()
    num = 1
    page = 1
    prod_list = []
    while 1:
        prod_input = []
        try:
            prod_input.append(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(9) > ul > li:nth-child(%s) > div > p.tit' % num).text) #prod Name
            prod_input.append(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(9) > ul > li:nth-child(%s) > div > p.price > span' % num).text) # price
            try:
                prod_input.append(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(9) > ul > li:nth-child(%s) > div > p.img > img' % num).get_attribute('src'))
            except NoSuchElementException:
                pass
            prod_input.append(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(9) > ul > li:nth-child(%s) > div > div > p > span' % num).text)
            prod_input[1] = prod_input[1].replace(',','')
            prod_input[1] = prod_input[1].replace('원','')
            prod_list.append(prod_input)
            print(prod_input)
            print(num)
            print(page)
            num += 1
            if num == 9:
                page += 1
                num = 1
                driver.execute_script("goodsPageController.movePage(%d);" % page)
                try:
                    if '검색된 상품이 없습니다.' in (driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[3]/div/div/div[4]/ul/li/p').text) :
                        print("Parse END")
                        break
                except NoSuchElementException:
                    print("TTTT")
                    continue
        except NoSuchElementException:
            print("Parse END")
            print("NoSuchElements")
            break
        except StaleElementReferenceException:
            print("Stale")
            time.sleep(1)
    print(prod_list)
    return prod_list


def ministop_parser():
    # Connect to page
    driver.get('https://www.ministop.co.kr/MiniStopHomePage/page/event/plus1.do')

    prod_list = []
    # 전부 불러오기! [1+1]
    num = 1
    while 1:
        try:
            driver.find_element_by_css_selector(
                '#section > div.inner.wrap.service1 > div.event_plus_list > div > a.pr_more').click()
            time.sleep(0.3)
        except NoSuchElementException:
            print("출력 끝...")
            break
    while 1:
        try:
            prod_input = []
            prod_input.append(driver.find_element_by_css_selector(
                '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%) > a > p').text)
            prod_input = prod_input[0].split('\n')
            try:
                prod_input.append(driver.find_element_by_css_selector(driver.find_element_by_css_selector(
                    '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a' % num).find_element_by_tag_name(
                    'img').get_attribute('src')))
            except NoSuchElementException:
                pass
            prod_input.append("1+1")
            prod_list.append(prod_input)
            num += 1
        except NoSuchElementException:
            break
    # 전부 불러오기! [2+1]
    driver.get('https://www.ministop.co.kr/MiniStopHomePage/page/event/plus2.do')
    num = 1
    while 1:
        try:
            driver.find_element_by_css_selector(
                '#section > div.inner.wrap.service1 > div.event_plus_list > div > a.pr_more').click()
            time.sleep(0.3)
        except NoSuchElementException:
            print("출력 끝...")
            break
    while 1:
        try:
            prod_input = []
            prod_input.append(driver.find_element_by_css_selector(
                '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%) > a > p').text)
            prod_input = prod_input[0].split('\n')
            try:
                prod_input.append(driver.find_element_by_css_selector(driver.find_element_by_css_selector(
                    '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a' % num).find_element_by_tag_name(
                    'img').get_attribute('src')))
            except NoSuchElementException:
                pass
            prod_input.append("2+1")
            prod_list.append(prod_input)
            num += 1
        except NoSuchElementException:
            break
    return prod_list

def seveneleven_parser():
    # Connect to page
    driver.get('http://www.7-eleven.co.kr/product/presentList.asp')
    prod_list = []
    # 전부 불러오기!
    while 1:
        try:
            driver.find_element_by_css_selector('#listUl > li.btn_more > a').click()
            time.sleep(0.3)
        except ElementNotInteractableException:
            print("More Ended...")
            break

    num = 2
    while 1:
        prod_input = []
        try:
            print(str(num-1)+"번째 상품 ->", end="")
            # 상품의 이름 및 가격 (line1: name, line2: price)
            prod_input.append(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).text)
            prod_input.append(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div/div/div[2]' % num).text)
            prod_input.append(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).find_element_by_tag_name('img').get_attribute('src'))
            prod_list.append(prod_input)
            num += 1
        except NoSuchElementException:
            print("parsing done")
            break

    # 2+1 상품으로 넘어가기
    driver.find_element_by_xpath('//*[@id="actFrm"]/div[3]/div[1]/ul/li[2]/a').click()

    # 전부 불러오기!
    while 1:
        try:
            driver.find_element_by_css_selector('#listUl > li.btn_more > a').click()
            time.sleep(0.3)
        except NoSuchElementException:
            print("More Ended...")
            break

    num = 2
    while 1:
        try:
            print(str(num - 1) + "번째 상품 ->", end="")
            # 상품의 이름 및 가격 (line1: name, line2: price)
            prod_input.append(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).text)
            prod_input.append(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div/div/div[2]' % num).text)
            prod_input.append(
                driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).find_element_by_tag_name(
                    'img').get_attribute('src'))
            prod_list.append(prod_input)
            num += 1
        except NoSuchElementException:
            print("parsing done")
            break
    return prod_list

if __name__ == '__main__':
    parsed_data = cu_parser()
    for data in parsed_data:
        Product(prodName=data[0], prodPrice=data[1], prodImg=data[2], prodEventType=data[3]).save()
    parsed_data = emart_parser()
    for data in parsed_data:
        Product2(prodName=data[0], prodPrice=data[1], prodImg=data[2], prodEventType=data[3]).save()
    parsed_data = gs25_parser()
    for data in parsed_data:
        Product3(prodName=data[0], prodPrice=data[1], prodImg=data[2], prodEventType=data[3]).save()
    parsed_data = ministop_parser()
    for data in parsed_data:
        Product4(prodName=data[0], prodPrice=data[1], prodImg=data[2], prodEventType=data[3]).save()
    parsed_data = seveneleven_parser()
    for data in parsed_data:
        Product5(prodName=data[0], prodPrice=data[1], prodImg=data[2], prodEventType=data[3]).save()
