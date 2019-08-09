from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException

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
# TODO: 덤증정은 귀찮아서 아직 안했음

# Connect to page
driver.get('https://www.ministop.co.kr/MiniStopHomePage/page/event/plus1.do')

# 전부 불러오기! [1+1]
num = 1
while 1:
    try:
        print(str(num) + "번째 상품 ->", end="")
        # 상품의 이름 및 가격 (line1: name, line2: price)
        print(driver.find_element_by_css_selector(
            '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a > p' % num).text)
        print(driver.find_element_by_css_selector(
            '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a' % num).find_element_by_tag_name(
            'img').get_attribute('src'))
        num += 1
        driver.find_element_by_css_selector('#section > div.inner.wrap.service1 > div.event_plus_list > div > a.pr_more').click()
        time.sleep(0.5)
    except NoSuchElementException:
        print("출력 끝...")
        break

# 전부 불러오기! [2+1]
driver.get('https://www.ministop.co.kr/MiniStopHomePage/page/event/plus2.do')
num = 1
while 1:
    try:
        print(str(num) + "번째 상품 ->", end="")
        # 상품의 이름 및 가격 (line1: name, line2: price)
        print(driver.find_element_by_css_selector(
            '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a > p' % num).text)
        print(driver.find_element_by_css_selector(
            '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a' % num).find_element_by_tag_name(
            'img').get_attribute('src'))
        num += 1
        driver.find_element_by_css_selector('#section > div.inner.wrap.service1 > div.event_plus_list > div > a.pr_more').click()
        time.sleep(0.5)
    except NoSuchElementException:
        print("출력 끝...")
        break

# 전부 불러오기! [N+1]
driver.get('https://www.ministop.co.kr/MiniStopHomePage/page/event/plus4.do')
num = 1
while 1:
    try:
        print(str(num) + "번째 상품 ->", end="")
        # 상품의 이름 및 가격 (line1: name, line2: price)
        print(driver.find_element_by_css_selector(
            '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a > p' % num).text)
        print(driver.find_element_by_css_selector(
            '#section > div.inner.wrap.service1 > div.event_plus_list > ul > li:nth-child(%s) > a' % num).find_element_by_tag_name(
            'img').get_attribute('src'))
        num += 1
        driver.find_element_by_css_selector('#section > div.inner.wrap.service1 > div.event_plus_list > div > a.pr_more').click()
        time.sleep(0.5)
    except NoSuchElementException:
        print("출력 끝...")
        break

