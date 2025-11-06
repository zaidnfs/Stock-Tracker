import requests
from datetime import datetime
from future.backports.datetime import timedelta
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
#CHANGE THEM ACCORDING TO YOURSELF
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_WEBSITE = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_WEBSITE = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH")

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : AV_API_KEY

}

yesterday = (datetime.now() - timedelta(2)).strftime('%y-%m-%d')
day_bef_yesterday = (datetime.now() - timedelta(3)).strftime('%y-%m-%d')

av_response = requests.get(url=STOCK_WEBSITE, params=parameters)
av_response.raise_for_status()
stock_data = av_response.json()

#Yesterday closing value
first_closing = float(stock_data["Time Series (Daily)"][f"20{yesterday}"]["4. close"])
#Day before yesterday closing value
second_closing = float(stock_data["Time Series (Daily)"][f"20{day_bef_yesterday}"]["4. close"])
closing_diff = abs(first_closing - second_closing)
diff_percent = int(closing_diff/second_closing * 100)
up_down = None
if first_closing > second_closing:
    up_down = "🔺"
elif second_closing > first_closing:
    up_down = "🔻"
else:
    up_down = "🟰"

if diff_percent > 0:
    parameters = {
         "apiKey" : NEWS_API_KEY,
        "q" : COMPANY_NAME,
        "from" : "2025-11-05",
        "to" : "2025-11-05",
        "language" : "en",
        "pageSize" : 3
    }
    news_response = requests.get(url=NEWS_WEBSITE, params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    required_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadlines: {article["title"]}.\n" for article in articles]

    for article in required_articles:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            #YOUR SERVICE SID
          messaging_service_sid="SERVICE SID",
          body=article,
            #YOUR NUMBER HERE
          to="YOUR NUMBER"
        )
        print(message.status)
else:
    pass


