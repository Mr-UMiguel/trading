import pandas as pd
from datetime import datetime

from controller.observer import MarketData
from model.BollingerBands import BollingerBandsStrategy
from utils.sim import GBM
from utils.performance import strategyPerfomance
from utils.plots import *


periods = 20
price = GBM() ## Simulación de una serie de precios.
hist_price = price.iloc[:periods].reset_index(drop=True)
new_price = price.iloc[periods:].reset_index(drop=True)

marketData = MarketData()
strategy = BollingerBandsStrategy(
    MarketData=marketData,
    hist_price=hist_price,
    periods=periods
)

## simulamos el "real-time" market data
for price in new_price:
    marketData.notify(price)

trades = strategy.get_trades()
data = pd.concat([new_price,trades],axis=1,keys=["Price","Trade"])

cummulative_returns = strategyPerfomance(data)

strategy_plot(data,periods)
performance_plot(cummulative_returns)




