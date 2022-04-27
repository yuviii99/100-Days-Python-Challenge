import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PRICE_API = "ALPHAVANTAGE API KEY"
NEWS_API_KEY = "NEWS API KEY"
TWILIO_SID = "TWILIO SID"
TWILIO_AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_PHONE = "TWILIO_PHONE"

stock_price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API,
}

stock_price = requests.get(url=STOCK_ENDPOINT, params=stock_price_params)
stock_price_data = stock_price.json()

daily_stock_price = stock_price_data["Time Series (Daily)"]
list_daily_stock_price = list(daily_stock_price.values())

yesterday_close = float(list_daily_stock_price[0]["4. close"])
day_before_yesterday_close = float(list_daily_stock_price[1]["4. close"])

price_difference = yesterday_close - day_before_yesterday_close
if price_difference > 0:
    upDown = "🔺"
else:
    upDown = "🔻"
price_difference = abs(price_difference)

diff_percentage = round((price_difference / yesterday_close) * 100)

if True:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY
    }
    news_articles = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_articles.json()["articles"]
    top_articles = articles[:3]

    formatted_messages = [
        f"{COMPANY_NAME}: {upDown}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in top_articles]
    # Sending SMS
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_messages:
        message = client.messages \
            .create(
            body=article,
            from_=TWILIO_PHONE,
            to="TO PHONE NUMBER"
        )
