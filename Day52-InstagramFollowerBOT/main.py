from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import time

WEB_DRIVER_PATH = "/Users/yuvi/Development/chromedriver"
SIMILAR_ACCOUNT = "YOUR CHOICE OF ACCOUNT"
USERNAME = "INSTAGRAM_USERNAME"
PASSWORD = "INSTAGRAM_PASSWORD"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))

    def login(self):
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        followers_count = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_count.click()
        time.sleep(5)

        pop_up = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            time.sleep(4)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_follower_bot = InstaFollower(WEB_DRIVER_PATH)
insta_follower_bot.login()
insta_follower_bot.find_followers()
insta_follower_bot.follow()
