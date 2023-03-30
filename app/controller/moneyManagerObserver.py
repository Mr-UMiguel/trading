class MoneyManager:
    "Observer design patter"

    def __init__(self):
        self._observers = []
        self.__cashAmount = 1000
        self.__cashCurncy = "USD"
    
    @property
    def cashAmount(self):
        return self.__cashAmount
    
    @cashAmount.setter
    def cashAmount(self):
        raise Exception("Cash Amount cannot be set")
    @cashAmount.deleter
    def cashAmount(self):
        raise Exception("Cash Amount cannot be deleted")
    
    @property
    def cashCurncy(self):
        return self.__cashCurncy
    
    @cashCurncy.setter
    def cashCurncy(self):
        raise Exception("Cash Curncy cannot be set")
    
    @cashCurncy.deleter
    def cashCurncy(self):
        raise Exception("Cash Curncy cannot be deleted")

    def attach(self,observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self,cashAmount):
        for observer in self._observers:
            observer.update(cashAmount)
