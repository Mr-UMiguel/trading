from event.histData import  HistoricalMarketData
import pandas as pd


def getHistData():
    app = HistoricalMarketData()
    app.connect("127.0.0.1", 7497, 0)
    app.run()
    return app

histData = pd.DataFrame(getHistData().getData())
# histData.set_index(pd.to_datetime(histData["date"]),inplace=True,drop=True)