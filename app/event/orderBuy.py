
from ibapi.contract import Contract
from ibapi.order import Order
from typing import Literal,Optional,Union

from .Order import OrderManager

class OrderBuy(OrderManager):
    def __init__(self):
        super(OrderBuy,self).__init__()
        
    
    def createContract(self,symbol:str,secType:str="STK",exchange:str="SMART",currency:str="USD") -> Order:
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency
        return contract
    
    def createOrder(self,quantity:int,orderType:Literal["MKT","STP LMT"]="STP LMT",
                        lmtPrice:float=None, stopPrice:Optional[float]=None):
        order = Order()
        order.action ="BUY"
        order.totalQuantity = quantity
        order.orderType = orderType
        if orderType == "STP LMT":
            order.lmtPrice  = lmtPrice
            order.auxPrice  = stopPrice
        return order