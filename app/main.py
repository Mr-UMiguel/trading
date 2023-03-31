## Built-in Packages
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

## External packages
import pandas as pd
from ibapi.contract import Contract
import time

from event.liveData import LiveMarketData, SimLiveData
from event.histData import HistoricalMarketData
from event.orderBuy import OrderBuy
from model.BollingerBands import BollingerBandsStrategy

### Algorithmic Trading 
## Ecopetrol  NYSE ADR

EC = Contract()
EC.symbol = "EC"
EC.secType = "STK"
EC.exchange = "SMART"
EC.currency = "USD"


def run_loop_EC():
    print("Running EC")
    # liveData =  LiveMarketData(contract=EC)
    # liveDataId = liveData.nextValidClientId()
    # liveData.connect("127.0.0.1",7497, clientId=liveDataId)

    histData = HistoricalMarketData(contract=EC,end_date="20230330 15:59:00 US/Eastern",duration="1 M",bar_size="5 mins",wts="TRADES")
    histdataId = histData.nextValidClientId()
    histData.connect("127.0.0.1",7497, clientId=histdataId)

    
    with ThreadPoolExecutor() as executor:
        future = executor.submit(histData.getData)
        hisDataResponse = future.result()
        executor.shutdown()
    
    closePricehist = pd.Series(hisDataResponse["close"]).iloc[:-97]
    closePricelive = pd.Series(hisDataResponse["close"]).iloc[-97:]

    liveData = SimLiveData(closePricelive)
    bbStrategy = BollingerBandsStrategy(
        MarketData=liveData,
        Contract= EC,
        hist_price=closePricehist,
        periods=20,
    )

    thread =  Thread(target=liveData.run)
    thread.start()


if __name__ == "__main__":
    run_loop_EC()





