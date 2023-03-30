from abc import ABC, abstractmethod
from ibapi.client import *
from ibapi.wrapper import *

class OrderManager(ABC,EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.orderId = 0
        self._contract = None   
        self._order =None

    def nextValidId(self, orderId: int):
        print("nextValidId triggered")
        contract = self._contract
        order = self._order
        self.orderId += orderId
        self.placeOrder(self.orderId , contract, order)
    
    @abstractmethod
    def createContract(self):
        pass

    @abstractmethod
    def createOrder(self):
        pass

    def sendOrder(self,contract:Contract,order:Order):
        self._contract = contract
        self._order = order
        super().run()

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print("** OPEN ORDER **")
        print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")
    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print("** ORDER STATUS **")
        print(f"orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillPrice: {avgFillPrice}, permId: {permId}, parentId: {parentId}, lastFillPrice: {lastFillPrice}, clientId: {clientId}, whyHeld: {whyHeld}, mktCapPrice: {mktCapPrice}")
        if status == "Filled":
            self.disconnect()
    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print("** EXECUTION DETAILS **")
        print(f"reqId: {reqId}, contract: {contract}, execution: {execution}")
    