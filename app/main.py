from model.BollingerBands import BollingerBandsStrategy
from controller.observer import MarketData

import numpy as np
import pandas as pd
from datetime import datetime

marketData = MarketData()
hist_price = np.random.normal(10,5,30)
date_range = pd.date_range(datetime.now(),periods=30)
bbs = BollingerBandsStrategy(MarketData=marketData,hist_price=hist_price,
                            periods=5,date_range=date_range)

def get_data():
    value = 0
    while value < 20:
        yield value
        value += 1

for price in get_data():
    marketData.notify(price)



