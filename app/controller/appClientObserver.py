from ibapi.client import *
from ibapi.wrapper import *
from queue import Queue


class IBApp(EClient,EWrapper):
    clientIds = 0
    def __init__(self):
        IBApp.clientIds += 1
        EClient.__init__(self,self)

    @classmethod
    def nextValidClientId(cls):
        return cls.clientIds