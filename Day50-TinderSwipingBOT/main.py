import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

USERNAME = "yuvisr1337@gmail.com"
PASSWORD = "Bholu#50960"

webdriver_path = "/Users/yuvi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(webdriver_path))

driver.get("https://tinder.com/")
time.sleep(7)

login_button = driver.find_element(By.LINK_TEXT, "Log in")
login_button.click()
time.sleep(2)

google_login = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Log in with Google']")

google_login.click()
time.sleep(5)

