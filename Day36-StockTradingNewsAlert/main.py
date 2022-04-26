import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PRICE_API = "4GTDUPDWAII85M6Y"
NEWS_API_KEY = "88caccdda52746a38028ad11b1d335bf"

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

price_difference = abs(yesterday_close - day_before_yesterday_close)

diff_percentage = (price_difference / yesterday_close) * 100
print(diff_percentage)

if diff_percentage > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY
    }
    news_articles = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_articles.json()["articles"]
    print(articles)
    top_articles = articles[0:3]



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
