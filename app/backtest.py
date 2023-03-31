from event.histData import  HistoricalMarketData
import pandas as pd
from ibapi.contract import Contract

from controller.marketDataObserver import MarketData
from model.BollingerBands import BollingerBandsStrategy
from utils.sim import GBM,OU
from utils.performance import strategyPerfomance
from utils.plots import *

EC = Contract()
EC.symbol = "EC"
EC.secType = "STK"
EC.exchange = "SMART"
EC.currency = "USD"

def getHistData():
    histData = HistoricalMarketData(contract=EC,end_date="20230330 15:59:00 US/Eastern",duration="1 M",bar_size="5 mins",wts="TRADES")
    histdataId = histData.nextValidClientId()
    histData.connect("127.0.0.1",7497, clientId=histdataId)
    histData.run()
    return histData

histData = pd.DataFrame(getHistData().getData())

print(histData)

prices = pd.Series(histData['close'])
periods = 20
marketData = MarketData()
strategy = BollingerBandsStrategy(
    MarketData=marketData,
    Contract=EC,
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




