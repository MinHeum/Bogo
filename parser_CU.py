from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bogo.settings')
import django
django.setup()
from parsed_data.models import Product


# Chrome 창을 띄우지 않고(headless 하게) driver 를 사용하기 위한 options 변수 선언 및 설정 그리고 driver 선언
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--disable-gpu")
driver = webdriver.Chrome('/Users/quatre/PycharmProjects/Bogo_hackathon/chromedriver', options=options)
driver.implicitly_wait(3)

# TODO: 불러오기가 끝났으니 제품명을 싸그리 크롤링해보자.
# TODO: 완료!!!
# TODO: 배열에 병렬로 append 하는게 가능이나 한가?
# TODO:  └ 일단 기능 다 완성하고 해보자 이건
# TODO: 상품명 불러왔으니 이젠 가격 크롤링 할 차례임
# TODO: 이미지 주소까지 다 긁어왔음
# TODO: 정복한 편의점들 ┐
# TODO: [[[세븐일레븐, CU, GS25, 이마트24, 미니스탑]]]
# TODO: 크롤링 기능을 함수로서 정의해보자!!!!!
# TODO: Parser 를 합칠것이다.



def cu_parser():
    # CU Parser
    # CU 페이지에 driver를 접속시킵니다.
    driver.get('http://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N')
    # 전체 페이지 LOAD 하기 (Test단계에서는 첫 번째 페이지만 로드)
    # while 1:
    #     try:
    #         driver.find_element_by_css_selector(
    #             '#contents > div.relCon > div.prodListWrap > div > div.prodListBtn-w > a').click()
    #         time.sleep(1)
    #     # ElementClickInterceptedException Exception 이 발생하면 1초 대기한다.
    #     except ElementClickInterceptedException:
    #         time.sleep(1)
    #     except StaleElementReferenceException:
    #         time.sleep(1)
    #     # NoSuchElementException 이 발생하면 더 이상 불러올 상품이 없다는 뜻이니 페이지 LOAD 를 중단한다.
    #     except NoSuchElementException:
    #         print("CU Parsing END")
    #         break

    # 순서대로 파싱하기위한 변수 선언
    num = 17
    col = 1
    prodcvs = "CU"
    prod_list = []
    while 1:
        prod_input = []
        try:
            print(str(int(num / 17) * 40 + col - 40) + "번째 상품 파싱")
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
                "#contents > div.relCon > div.prodListWrap > ul > li:nth-child(1) > ul > li").text)
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


# 이 명령어는 이 파일이 import 가 아닌 python 에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__ == '__main__':
    parsed_data = cu_parser()
    for data in parsed_data:
        Product(prodName=data[0], prodPrice=data[1], prodImg=data[2], prodEventType=data[3], prodCVS="CU").save()
