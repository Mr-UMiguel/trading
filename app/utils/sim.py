import pandas  as pd
import numpy as np
from datetime import datetime

def GBM():
    alpha, sigma, T, n = 0.7, 0.3, 1, 1000
    dt = T/n
    y = np.ones(n)
    for t in range(1,n):
        Z = np.random.randn() # de (6.5)
        #Expresión exacta del MBG
        y[t] = y[t-1] *  np.exp((alpha - ((sigma**2)/2))*dt + sigma*np.sqrt(dt)*Z)

    date_range = pd.date_range(datetime.now(),periods=n)
    y =  pd.Series(y,index=date_range)
    return y