from event.histData import  HistoricalMarketData
import pandas as pd

from controller.marketDataObserver import MarketData
from model.BollingerBands import BollingerBandsStrategy
from utils.sim import GBM,OU
from utils.performance import strategyPerfomance
from utils.plots import *


def getHistData():
    app = HistoricalMarketData()
    app.connect("127.0.0.1", 7497, 0)
    app.run()
    return app

histData = pd.DataFrame(getHistData().getData())

prices = histData['close']
periods = 20
marketData = MarketData()
strategy = BollingerBandsStrategy(
    MarketData=marketData,
    hist_price=prices,
    periods=periods,
    risk=0.05
)

## simulamos el "real-time" market data
for price in prices:
    marketData.notify(price)

trades = strategy.get_trades()
data = pd.concat([prices,trades],axis=1,keys=["Price","Trade"])


cummulative_returns = strategyPerfomance(data)

strategy_plot(data,periods)
performance_plot(cummulative_returns)




