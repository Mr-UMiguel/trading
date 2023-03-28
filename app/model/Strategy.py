from abc import ABC, abstractmethod
from controller.marketDataObserver import MarketData

class TradingStrategy(ABC):
    "Strategy design pattern"

    def __init__(self, MarketData:MarketData):
        self.MarketData = MarketData
        self.MarketData.attach(self)
        super(TradingStrategy, self).__init__()

    def buy(self,price):
        # print(f"Buy: {price}")
        # self.create_order()
        pass
    
    def sell(self,price):
        # print(f"Sell: {price}")
        # self.create_order()
        pass
    
    def keep(self,price):
        pass

    @abstractmethod #update must be overriden by subclasses
    def update(self,price):
        pass

    @abstractmethod
    def analyzeData(self,price):
        pass

    def create_order(self,ticker,orderType,quantity,price):
        pass
        

    



