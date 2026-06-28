import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "KEY"
NEWS_API = "API"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : ALPHA_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
new_list = [value for (key,value) in data.items()]
yesterday_closing_price = float(new_list[0]["4. close"])





day_before_yes = float(new_list[1]["4. close"])



difference = abs(yesterday_closing_price - day_before_yes)



diff_percent = (difference/ yesterday_closing_price) * 100


if diff_percent > 2 :
    news_params = {
        "apiKey" : NEWS_API,
        "qInTitle" : COMPANY_NAME
    }
    
    r = requests.get(url=NEWS_ENDPOINT,params=news_params)
    news_data = r.json()["articles"]
    three_news = news_data[:3]
    print(three_news)






 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

