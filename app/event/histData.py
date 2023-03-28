from ibapi.client import *
from ibapi.wrapper import *
from queue import Queue

class HistoricalMarketData(EClient,EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = Queue()
    
    def nextValidId(self, orderId:int):
        mycontract = Contract()
        mycontract.symbol = "EC"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqHistoricalData(orderId, mycontract, "20230327 15:59:00 US/Eastern", "6 D", "5 mins", "TRADES", 1, 1, False, [])

    def historicalData(self, requestId, bar):
        self.data.put({
            'date':bar.date,
            'open':bar.open,
            'high':bar.high,
            'low':bar.low,
            'close':bar.close,
            'volume':bar.volume,
            'barCount':bar.barCount
        })

    def historicalDataEnd(self, reqId, start, end):
        print(f"End of historical Data: {start}, End: {end}")
        self.data.put(None)
        self.disconnect()

    def getData(self) -> dict:
        listQueue = list(self.data.queue)
        cleanData = {
            'date': [i['date'] for i in listQueue if i is not None],
            'open': [i['open'] for i in listQueue if i is not None],
            'high': [i['high'] for i in listQueue if i is not None],
            'low':  [i['low'] for i in listQueue if i is not None],
            'close':[i['close'] for i in listQueue if i is not None],
            'volume':[i['volume'] for i in listQueue if i is not None],
            'barCount':[i['barCount'] for i in listQueue if i is not None]
        }
        return cleanData