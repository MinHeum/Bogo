from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:/tempfileforprojects/chromedriver.exe')
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

# Connect to page
driver.get('http://www.7-eleven.co.kr/product/presentList.asp')

# 전부 불러오기!
while 1:
    try:
        driver.find_element_by_css_selector('#listUl > li.btn_more > a').click()
        time.sleep(0.5)
    except ElementNotInteractableException:
        print("More Ended...")
        break

num = 2
while 1:
    try:
        print(str(num-1)+"번째 상품 ->", end="")
        # 상품의 이름 및 가격 (line1: name, line2: price)
        print(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).text)
        print(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).find_element_by_tag_name('img').get_attribute('src'))
        num += 1
    except NoSuchElementException:
        print("은 없다 ㅎ")
        break

# 2+1 상품으로 넘어가기
driver.find_element_by_xpath('//*[@id="actFrm"]/div[3]/div[1]/ul/li[2]/a').click()

# 전부 불러오기!
while 1:
    try:
        driver.find_element_by_css_selector('#listUl > li.btn_more > a').click()
        time.sleep(0.5)
    except NoSuchElementException:
        print("More Ended...")
        break

num = 2
while 1:
    try:
        print(str(num-1)+"번째 상품 ->", end="")
        # 상품의 이름 및 가격 (line1: name, line2: price)
        print(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).text)
        print(driver.find_element_by_xpath('//*[@id="listUl"]/li[%s]/div' % num).find_element_by_tag_name('img').get_attribute('src'))
        num += 1
    except NoSuchElementException:
        print("은 없음 ㅎ")
        break

