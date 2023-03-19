import pandas as pd
import numpy as np
from typing import Union


from .Strategy import TradingStrategy

class BollingerBandsStrategy(TradingStrategy):

    def __init__(self,MarketData, hist_price:Union[pd.Series,np.ndarray],periods:int,nstd:int=2,date_range:pd.DatetimeIndex=None):
        self.periods = periods
        self.hist_price = hist_price
        self.nstd = nstd
        if type(self.hist_price) == pd.Series:
            self.validate_series_index()
        else:
            if date_range is None:
                raise TypeError(f"If price is a {np.ndarray} object then BollingerBandsStrategy(date_range) must be specified")
        super(BollingerBandsStrategy,self).__init__(MarketData)


    def update(self,price:float):
        self.analyzeData(price)

    def analyzeData(self,price:float):
        self.hist_price = np.concatenate([self.hist_price,np.array([price])])[1:]
        ma = self.calc_sma(self.hist_price)
        std = self.calc_smsd(self.hist_price)

        upper_band = ma + std * self.nstd
        lower_band = ma - std * self.nstd

        if price > upper_band:
            self.sell(price)
        
        elif price < lower_band:
            self.buy(price)


    def calc_smsd(self,serie):
        "simple moving standard deviation"
        if type(serie) == pd.Series:
            return self.serie.rolling(self.periods).std()
        else:
            window = self.periods
            return np.sqrt(np.convolve(np.square(serie - np.mean(serie)),np.ones(window)/window,mode="valid"))[0]

    def calc_sma(self,serie):
        "simple moving average"
        if type(serie) == pd.Series:
            return serie.rolling(self.periods).mean()
        else:
            window = self.periods
            return np.convolve(serie,np.ones(window)/window,mode="valid")[0]

    def validate_series_index(self):
        assert type(self.hist_price.index) == pd.DatetimeIndex, f"{self.hist_price.__name__} index must be {pd.DatetimeIndex}"


    
