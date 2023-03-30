from .Order import OrderManager

class OrderSell(OrderManager):
    def __init__(self,moneyManager):
        super(OrderSell, self).__init__(moneyManager)
        self.totalSellOrdersPerDay = 0

    def sendOrder(self,contract,order):
        if self.totalSellOrdersPerDay < 4:
            super().sendOrder(contract,order)
            