from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient,EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}
    
    def nextValidId(self, orderId:int):
        mycontract = Contract()
        mycontract.symbol = "EC"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqHistoricalData(orderId, mycontract, "20230315 15:59:00 US/Eastern", "2 D", "5 mins", "TRADES", 1, 1, False, [])

    def historicalData(self, requestId, bar):
        self.data['Date'].append(bar.Date)
        self.data['Open'].append(bar.Open)
        self.data['High'].append(bar.High)
        self.data['Low'].append(bar.Low)
        self.data['Close'].append(bar.Close)
        self.data['Volume'].append(bar.Volume)
        self.data['BarCount'].append(bar.BarCount)

        print(f"Historical Data: {bar}")

    def historicalDataEnd(self, reqId, start, end):
        print(f"End of historical Data: {start}, End: {end}")

    def get_data(self) ->dict:
        return self.data