
from ibapi.contract import Contract
from ibapi.order import Order
from typing import Literal,Optional,Union
from .Order import OrderManager

class OrderSell(OrderManager):
    def __init__(self,contract:Contract):
        super(OrderSell,self).__init__(contract)
        
    
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
        order.action ="SELL"
        order.totalQuantity = quantity
        order.orderType = orderType
        if orderType == "STP LMT":
            order.lmtPrice  = lmtPrice
            order.auxPrice  = stopPrice
        return order