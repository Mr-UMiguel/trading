from event.liveData import LiveMarketData
from event.orderBuy import OrderBuy
from threading import Thread
import time


def main():
    # Create a new LiveMarketData object
    marketData = LiveMarketData()
    marketData.connect("127.0.0.1",7497, clientId=0)
    thread1 =  Thread(target=marketData.run)
    thread1.start()

    buy = OrderBuy()
    buy.connect("127.0.0.1",7497, clientId=1)
    contract = buy.createContract(symbol="RIO",currency="AUD")
    order = buy.createOrder(quantity=1,lmtPrice=115.25,stopPrice=115.20)

    thread2 = Thread(target=buy.sendOrder,args=(contract,order))
    thread2.start() 
    thread2.join()

    


if __name__ == "__main__":
    main()