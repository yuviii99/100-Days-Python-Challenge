from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/yuvi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))


driver.get("https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/ref=sr_1_1_sspa?crid=4JKKU9R2XF1B&keywords=iphone%2B13&qid=1652030188&sprefix=iphone%2B1%2Caps%2C232&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVUNJOEtER0VWRFJHJmVuY3J5cHRlZElkPUEwMDg1MDgzMk8xQk1TSTNST1lGTSZlbmNyeXB0ZWRBZElkPUEwMzMzNDc2Q0NKRDQ2R1IwM0ozJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")
price = driver.find_element(By.CSS_SELECTOR, "span.apexPriceToPay")
print(price.text)

driver.quit()
