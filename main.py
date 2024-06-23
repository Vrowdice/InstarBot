from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException

import time
import random

stoped_id = 'id'
stoped_pw = 'password'

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.instagram.com/'
driver.get(url)
time.sleep(1)

def Login() :
    idInput = driver.find_elements(By.CLASS_NAME, '_aa4b')
    idInput[0].send_keys(stoped_id)
    idInput[1].send_keys(stoped_pw)
    idInput[1].send_keys(Keys.ENTER)
    time.sleep(10)

    driver.find_elements(By.XPATH, "//*[contains(text(), '나중에 하기')]")[0].click()
    time.sleep(2)
    driver.find_elements(By.CLASS_NAME, '_a9--')[0].click()
    time.sleep(1)

def find_like():
    attempts = 0
    while attempts < 10:
        try:
            element = driver.find_element(By.XPATH, '//*[@aria-label="좋아요"]')
            return element
        except StaleElementReferenceException:
            random.uniform(1.0, 2.0)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            attempts += 1
    return None

def Like() :
    for i in range(0, 50) :
        try:
            likeThing = find_like()
            likeThing.click()
            time.sleep(random.uniform(1.0, 3.0))
        except StaleElementReferenceException:
            i = i + 1
            continue
        except :
            break

def Follow() :
    driver.execute_script("window.scrollTo(0, 50);")
    time.sleep(5)
    
    driver.find_element(By.XPATH, "//*[contains(text(), '모두 보기')]").click()
    time.sleep(4)
    followThing = driver.find_elements(By.XPATH, "//*[contains(text(), '팔로우')]")
    for val in followThing :
        try : 
            val.click()
        except :
            driver.find_element(By.XPATH, '//*[@aria-label="홈"]').click()
        time.sleep(random.uniform(1.0, 2.0))
    
    driver.find_element(By.XPATH, '//*[@aria-label="홈"]').click()

Login()
time.sleep(5)
Like()
time.sleep(5)
Follow()
