import pandas as pd
import numpy as np
from typing import Union


from .Strategy import TradingStrategy

class BollingerBandsStrategy(TradingStrategy):

    def __init__(self,MarketData, hist_price:pd.Series,periods:int,nstd:float=2.0):
        assert len(hist_price) <= periods, "lenght(hist_price) must be equal or grather than periods"
        self.hist_price = hist_price[-periods:] # solo nos interesa los últimos periodos
        self.periods = periods
        self.nstd = nstd

        self.trades = []
        super(BollingerBandsStrategy,self).__init__(MarketData) # supermonemos la clase padre

    def update(self,price:float):
        trade = self.analyzeData(price)
        if trade == 1:
            self.buy(price)
        elif trade == -1:
            self.sell(price)
        else:
            self.keep(price)
        
        self.trades.append(trade)

    def analyzeData(self,price:float):
        self.hist_price = pd.concat([self.hist_price,pd.Series([price])],axis=0)[1:]
        sma = self.calc_sma(self.hist_price)
        sstd = self.calc_smsd(self.hist_price)

        upper_band = sma + sstd * self.nstd
        lower_band = sma - sstd * self.nstd

        signal = 0
        if price < lower_band:
            # self.buy(price)
            signal = 1
        elif price > upper_band:
            signal = -1
        else:
            signal = 0


        return signal
    
    def calc_smsd(self,serie):
        "simple moving standard deviation"
        return serie.std()

    def calc_sma(self,serie):
        "simple moving average"
        return serie.mean()
    
    def get_trades(self)->pd.Series:
        return pd.Series(self.trades)

