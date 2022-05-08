from bs4 import BeautifulSoup
import smtplib
import requests
import lxml
from re import sub
from decimal import Decimal

USER_ID = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'

TARGET_PRICE = 70000.00
URL = "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/ref=sr_1_1_sspa?crid=4JKKU9R2XF1B&keywords=iphone+13&qid=1652030188&sprefix=iphone+1%2Caps%2C232&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVUNJOEtER0VWRFJHJmVuY3J5cHRlZElkPUEwMDg1MDgzMk8xQk1TSTNST1lGTSZlbmNyeXB0ZWRBZElkPUEwMzMzNDc2Q0NKRDQ2R1IwM0ozJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

HEADERS = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

response = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(response.content, 'lxml')
price = soup.find(name='span', class_="a-offscreen").getText()

# Convert currency string into decimal value
value = Decimal(sub(r'[^\d.]', '', price))

if value <= TARGET_PRICE:
    message = f"The price of {soup.title.string} is below {TARGET_PRICE}. Buy Now!\n{URL}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_ID, password=PASSWORD)
        connection.sendmail(
            from_addr=USER_ID,
            to_addrs="RECEIVER EMAIL",
            msg=f"Subject: LOW PRICE ALERT!\n\n{message}"
        )


