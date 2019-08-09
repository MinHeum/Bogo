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

# Connect to page
driver.get('http://gs25.gsretail.com/gscvs/ko/products/event-goods')

# GS는 안타깝게도 다른 방식으로 불러와야한다.
num = 1
col = 0
while 1:
    try:
        print((num+(col*8), "번째 상품 ->"))
        # 상품의 이름 및 가격 (line1: name, line2: price, line3: img)
        print(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(3) > ul > li:nth-child(%s) > div > p.tit' % num).text)
        print(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(3) > ul > li:nth-child(%s) > div > p.price' % num).text)
        try:
            print(driver.find_element_by_css_selector('#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(3) > ul > li:nth-child(%s) > div > p.img' % num).find_element_by_tag_name('img').get_attribute('src'))
        except NoSuchElementException:
            pass
        num += 1
        if num is 8:
            col += 1
            num = 1
            driver.execute_script('goodsPageController.moveControl(1);')
    except NoSuchElementException:
        print("은 없다 ㅎ")
        break
    except StaleElementReferenceException:
        time.sleep(2)
