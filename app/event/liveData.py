from controller.marketDataObserver import MarketData


from ibapi.client import *
from ibapi.wrapper import *

class LiveMarketData(EClient,EWrapper,MarketData):
    def __init__(self):
        EClient.__init__(self, self)
        MarketData.__init__(self)
    
    def run(self):
        super().connect("127.0.0.1", 7497,1000)
        try:
            super().run()
        except KeyboardInterrupt:
            print("\n\nKeyboardInterrupt")
        finally:
            "Finally block"


    def nextValidId(self, orderId:int):
        mycontract = Contract()
        mycontract.symbol = "EC"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqMarketDataType(4)
        self.reqMktData(orderId, mycontract, "", 0, 0, [])

    def tickPrice(self, reqId, tickType, price, attrib):
        self.notify(price)
        print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attrib: {attrib}")

    def tickSize(self, reqId, tickType, size):
        print(f"tickSize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, size: {size}")

