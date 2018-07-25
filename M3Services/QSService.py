import requests
import json
class QSService:
    def __init__(self):
        self.API_KEY = 'MCAF9B429I44328U'
        self.HOST = 'https://www.alphavantage.co/'
    def test_call(self, stock_code):
        url = self.HOST + 'query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=NSE:'+stock_code+'&outputsize=full&apikey=' + self.API_KEY
        response = requests.get(url,params=None)
        if response.ok:
            jData=json.loads(response.content)
            timeSeries=jData["Time Series (Daily)"].values()
            latestPrice=next(iter(timeSeries))
            print("open price of this stock today is: "+latestPrice["1. open"])
            print("closed price of this stock today is: " + latestPrice["4. close"])
        
