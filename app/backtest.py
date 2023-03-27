import pandas as pd
from datetime import datetime

from controller.observer import MarketData
from model.BollingerBands import BollingerBandsStrategy
from utils.sim import GBM
from utils.performance import strategyPerfomance
from utils.plots import *

# data = pd.read_csv("./source/CHILE.csv")

# data = pd.read_csv("app\source\CHILE.csv")


periods = 20
prices = GBM() ## Simulación de una serie de precios.
# prices = data['Adj Close']

print(prices)

marketData = MarketData()
strategy = BollingerBandsStrategy(
    MarketData=marketData,
    hist_price=prices,
    periods=periods
)

## simulamos el "real-time" market data
for price in prices:
    marketData.notify(price)

trades = strategy.get_trades()
data = pd.concat([prices,trades],axis=1,keys=["Price","Trade"])


cummulative_returns = strategyPerfomance(data)

strategy_plot(data,periods)
performance_plot(cummulative_returns)




