from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
driver = webdriver.Chrome('/Users/quatre/PycharmProjects/Bogo_hackathon/chromedriver')
driver.implicitly_wait(3)

# TODO: 불러오기가 끝났으니 제품명을 싸그리 크롤링해보자.
# TODO: 완료!!!
# TODO: 배열에 병렬로 append 하는게 가능이나 한가?
# TODO:  └ 일단 기능 다 완성하고 해보자 이건
# TODO: 상품명 불러왔으니 이젠 가격 크롤링 할 차례임
# TODO:=======================================================
# TODO:=======================D O N E ! ======================
# TODO:=======================================================
# TODO: 이미지 주소까지 다 긁어왔음
# TODO: 정복한 편의점들 ┐
# TODO: [[[세븐일레븐, CU, GS25, 이마트24, 미니스탑]]]
# TODO: 이마트24의 경우에는 1+1, 2+1 뿐만 아니라, sale 상품과 덤증정상품으로 상품이름이 이상하게 출력되는 경우가 있음
# TODO: 덤증정의 경우에는 _ 로 split 해서 나누면 됨

# Connect to page
driver.get('https://www.emart24.co.kr/product/eventProduct.asp')

# 이마트24 또한 안타깝게도 다른 방식으로 불러와야한다.
num = 1
col = 0
while 1:
    try:
        print(num+(col*15), "번째 상품 파싱")
        # 상품의 이름 및 가격 (line1: name, line2: price, line3: img)
        print(driver.find_element_by_css_selector('#regForm > div.section > div.eventProduct > div.tabContArea > ul > li:nth-child(%s) > div > p.productDiv' % num).text)
        print(driver.find_element_by_css_selector('#regForm > div.section > div.eventProduct > div.tabContArea > ul > li:nth-child(%s) > div > p.price' % num).text)
        try:
            print(driver.find_element_by_css_selector('#regForm > div.section > div.eventProduct > div.tabContArea > ul > li:nth-child(%s) > div > p.productImg' % num).find_element_by_tag_name('img').get_attribute('src'))
        except NoSuchElementException:
            pass
        eventtype = driver.find_element_by_xpath('//*[@id="regForm"]/div[2]/div[3]/div[2]/ul/li[8]/div/div/p/img').get_attribute('alt')
        print(eventtype)
        if '2 + 1 뱃지'in eventtype:
            eventtype = '2+1'
        elif 'SALE 뱃지'in eventtype:
            eventtype = 'sale'
        elif 'X2 더블 뱃지'in eventtype:
            eventtype = 'dum'
        elif '1 + 1 뱃지 이미지'in eventtype:
            eventtype = '1+1'
        elif '3 + 1 뱃지'in eventtype:
            eventtype = '3+1'
        else:
            eventtype = 'error!'
        print(eventtype)
        num += 1
        if num is 16:
            col += 1
            num = 1
            driver.find_element_by_css_selector('#regForm > div.section > div.eventProduct > div.paging > a.next.bgNone > alt').click()
    except NoSuchElementException:
        print("은 없다 ㅎ")
        break
    except StaleElementReferenceException:
        time.sleep(2)
