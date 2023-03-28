import pandas as pd
import numpy as np
from queue import Queue



from .Strategy import TradingStrategy

class BollingerBandsStrategy(TradingStrategy):

    def __init__(self,MarketData, hist_price:pd.Series,periods:int,nstd:float=2.0,risk:float=0.01):
        assert len(hist_price) > periods, "lenght(hist_price) must be equal or grather than periods"
        self.hist_price = hist_price[:periods] # solo nos interesa los últimos periodos
        self.periods = periods
        self.nstd = nstd
        self.risk = risk


        self.long_positions = Queue()
        self.short_positions = Queue()
        self.trades = []
        super(BollingerBandsStrategy,self).__init__(MarketData) # supermonemos la clase padre

    def update(self,price:float):
        trade = self.analyzeData(price)
        match trade:
            case 1:
                self.long_positions.put(price)
                self.buy(price)
            case 2:
                self.sell(price)
            case 3:
                self.sell(price)
            case -1:
                self.short_positions.put(price)
                self.sell(price)
            case -2:
                self.buy(price)
            case -3:
                self.buy(price)
            case 0:
                self.keep(price)
        
        self.trades.append(trade)

    def analyzeData(self,price:float):
        self.hist_price = pd.concat([self.hist_price,pd.Series([price])],axis=0)[1:]
        sma = self.calc_sma(self.hist_price)
        sstd = self.calc_smsd(self.hist_price)

        upper_band = sma + sstd * self.nstd
        lower_band = sma - sstd * self.nstd

        sl_long = self.stop_long(price)
        tp_long = self.take_long(price,sma)


        sl_short = self.stop_short(price)
        tp_short = self.take_short(price,sma)

        signal = 0
        if tp_long == False:
            if price < lower_band:
                if sl_long==True:
                    signal = 2
                else:
                    if 1 not in self.trades[-3:]:
                        signal = 1
        else:
            signal = 3

        # if tp_short == False:
        #     if price > upper_band:
        #         if sl_short:
        #             signal = -2
        #         else:
        #             if -1 not in self.trades[-3:]:
        #                 signal = -1
        # else:
        #     signal = -3

        return signal


    def take_long(self,price,sma):
        nlongs = len(self.long_positions.queue)
        tp = False
        if nlongs > 0:
            if price > sma:
                self.long_positions.get()
                tp = True

        return tp

    def take_short(self,price,sma):
        nshorts = len(self.short_positions.queue)
        tp = False
        if nshorts > 0:
            if price < sma:
                self.short_positions.get()
                tp = True

        return tp

    def stop_long(self,price):
        nlongs = len(self.long_positions.queue)
        sl = False
        if nlongs > 0:
            for pricet_1 in self.long_positions.queue:
                ret = (price/pricet_1) - 1
                if ret <= -self.risk:
                    self.long_positions.get()
                    sl = True
                    break
        
        return sl



    def stop_short(self,price):
        nshorts = len(self.short_positions.queue)
        sl = False
        if nshorts > 0:
            for pricet_1 in self.short_positions.queue:
                ret = (price/pricet_1) - 1
                if ret >= self.risk:
                    self.short_positions.get()
                    sl = True
                    break
        
        return sl

    def calc_smsd(self,serie):
        "simple moving standard deviation"
        return serie.std()

    def calc_sma(self,serie):
        "simple moving average"
        return serie.mean()
    
    def get_trades(self)->pd.Series:
        return pd.Series(self.trades)

