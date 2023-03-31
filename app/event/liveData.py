from controller.marketDataObserver import MarketData
from controller.appClientObserver import IBApp
from ibapi.client import *
from ibapi.wrapper import *
import time

class LiveMarketData(IBApp,MarketData):
    def __init__(self,contract:Contract,dataType:int=1):
        super().__init__()
        MarketData.__init__(self)
        self.__contract = contract
        self.__dataType = dataType

    def nextValidId(self, orderId:int):

        self.reqMarketDataType(self.__dataType)
        self.reqMktData(orderId, self.__contract , "", False, False, [])

    def tickPrice(self, reqId, tickType, price, attrib):
        # print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attrib: {attrib}")
        self.notify(price)
    def tickSize(self, reqId, tickType, size):
        print(f"tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}")

class SimLiveData(MarketData):
    def __init__(self,serie):
        super().__init__()
        MarketData.__init__(self)
        self._serie = serie
        

    def run(self):
        def gen(serie):
            for p in serie:
                time.sleep(1)
                yield p

        g = gen(serie=self._serie)
        while True:
            try:
                value = next(g)
                print(f"Price: {value}")
                self.notify(value)
            except StopIteration:
                break