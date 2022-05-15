import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


# Constants
FORM_URL = "YOUR G FORM LINK" # Edit XPATHS Accordingly
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
WEB_DRIVER_PATH = "Your webdriver path"

# Scraping Renting Data
driver = webdriver.Chrome(service=Service(WEB_DRIVER_PATH))
driver.get(ZILLOW_URL)
soup = BeautifulSoup(driver.page_source, 'html.parser')


address_tags = soup.find_all(name='address', class_='list-card-addr')
address_list = []
for address in address_tags:
    address_list.append(address.getText())

price_tags = soup.find_all(name='div', class_='list-card-price')
price_list = []
for price in price_tags:
    price_list.append(price.getText()[0:6])

link_tags = soup.find_all(name='a', class_='list-card-img')
link_list = []
for link in link_tags:
    link_text = link.get('href')
    if 'http' not in link_text:
        link_list.append(f"https://www.zillow.com{link_text}")
    else:
        link_list.append(link_text)

for i in range(len(price_list)):
    driver.get(url=FORM_URL)
    time.sleep(5)

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[i])

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[i])

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_list[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
