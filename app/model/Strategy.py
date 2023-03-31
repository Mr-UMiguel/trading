from abc import ABC, abstractmethod
from threading import Thread

from controller.marketDataObserver import MarketData
from event.Order import Order
from event.orderBuy import OrderBuy
from event.orderSell import OrderSell

class TradingStrategy(ABC):
    "Strategy design pattern"

    def __init__(self, MarketData:MarketData,contract,orderBuy = OrderBuy, orderSell = OrderSell):
        self.MarketData = MarketData
        self.MarketData.attach(self)
        self.contract = contract
        self.orderBuy = orderBuy
        self.orderSell = orderSell
        super(TradingStrategy, self).__init__()

    def buy(self,price):
        print(f"BUY: {self.contract}")
        buy = self.orderBuy(self.contract)
        buyId = buy.nextValidClientId()
        buy.connect("127.0.0.1",7497,buyId)
        order = buy.createOrder(quantity=10,orderType="MKT")
        thread = Thread(target=buy.sendOrder,args=(order,))
        thread.start()
    def sell(self,price):
        print(f"Sell: {self.contract}")
        sell = self.orderSell(self.contract)
        sellId = sell.nextValidClientId()
        sell.connect("127.0.0.1",7497,sellId)
        order = sell.createOrder(quantity=10,orderType="MKT")
        thread = Thread(target=sell.sendOrder, args=(order,))
        thread.start()

    def keep(self,price):
        pass

    @abstractmethod #update must be overriden by subclasses
    def update(self,price):
        pass

    @abstractmethod
    def analyzeData(self,price):
        pass

    



