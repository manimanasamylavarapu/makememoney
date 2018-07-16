import datetime
import requests
import json

from pip._vendor.distlib.compat import raw_input

stockCode = raw_input('enter the NSE stock name to see it\'s current price')

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=NSE:'+stockCode+'&outputsize=full&apikey=MCAF9B429I44328U'
myResponse = requests.get(url,params=None)
#todayzDate=datetime.datetime.today().strftime('%Y-%m-%d')

if myResponse.ok:
    jData=json.loads(myResponse.content)
    timeSeries=jData["Time Series (Daily)"].values()
    latestPrice=next(iter(timeSeries))
    print("open price of this stock today is: "+latestPrice["1. open"])
    print("closed price of this stock today is: " + latestPrice["4. close"])
