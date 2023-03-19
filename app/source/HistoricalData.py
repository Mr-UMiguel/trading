from ibapi.client import *
from ibapi.wrapper import *

class TestApp(EClient,EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    
    def nextValidId(self, orderId:int):
        mycontract = Contract()
        mycontract.symbol = "EC"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqHistoricalData(orderId, mycontract, "20230315 15:59:00 US/Eastern", "2 D", "5 mins", "TRADES", 1, 1, False, [])

    def historicalData(self, requestId, bar):
        print(f"Historical Data: {bar}")

    def historicalDataEnd(self, reqId, start, end):
        print(f"End of historical Data: {start}, End: {end}")

app = TestApp()
app.connect("127.0.0.1", 7497,1000)
app.run()