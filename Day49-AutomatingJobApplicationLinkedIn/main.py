import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.support.select import Select

webdriver_path = "/Users/yuvi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(webdriver_path))

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.maximize_window()

sign_in_key = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_key.click()
time.sleep(5)

email_field = driver.find_element(By.NAME, "session_key")
password_field = driver.find_element(By.NAME, "session_password")
email_field.send_keys("yuvisr1337@gmail.com")
password_field.send_keys("Chutiya#262010")
button = driver.find_element(By.CSS_SELECTOR, "div.login__form_action_container button")
button.click()
time.sleep(5)

apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
apply_button.click()
time.sleep(5)

phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("1234567890")

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
time.sleep(4)

next_button = driver.find_elements(By.CSS_SELECTOR, "footer button")
next_button[1].click()
time.sleep(4)

proficiency = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3069616206,54225299,multipleChoice)"]')
dropdown = Select(proficiency)
dropdown.select_by_index(3)
time.sleep(5)

experience = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3069616206,54225283,multipleChoice)"]')
DD = Select(experience)
DD.select_by_index(1)

review_button = driver.find_elements(By.CSS_SELECTOR, "footer button")
review_button[1].click()
time.sleep(5)

submit_btn = driver.find_elements(By.CSS_SELECTOR, "footer button")
submit_btn[1].click()
