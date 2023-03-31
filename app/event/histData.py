from controller.appClientObserver import IBApp
from ibapi.client import *
from ibapi.wrapper import *
from queue import Queue

class HistoricalMarketData(IBApp):
    def __init__(self,contract:Contract,end_date:str,duration:str,bar_size:str,wts:str):
        super().__init__()
        self.data = Queue()
        self.done = False

        self.__contract = contract
        self.__end_date = end_date
        self.__duration = duration
        self.__bar_size = bar_size
        self.__wts      = wts
    
    def nextValidId(self, orderId:int):

        self.reqHistoricalData(orderId, self.__contract, self.__end_date, self.__duration, 
                                        self.__bar_size, self.__wts, 1, 1, False, [])

    def historicalData(self, requestId, bar):
        self.data.put({
            'reqId':requestId,
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
        self.done = True
        self.disconnect()

    def getData(self) -> dict:
        super().run()
        
        while self.done == False:
            continue

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
    
