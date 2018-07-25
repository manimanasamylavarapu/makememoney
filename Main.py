from M3Services import QSService
from pip._vendor.distlib.compat import raw_input

qs = QSService()
stockCode = raw_input('enter the NSE stock name to see it\'s current price:')
qs.test_call(stockCode)
