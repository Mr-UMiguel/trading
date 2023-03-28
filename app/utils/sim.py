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

    return pd.Series(y)

def OU():
    # Define parameters
    theta = 0.1  # mean reversion strength
    mu = 0.5     # mean reversion level
    sigma = 0.1  # volatility of the process
    T = 1        # simulation time
    N = 1000  # number of time steps
    dt = T/N    # time step

    # Initialize arrays
    x = np.zeros(N)   # price series
    x[0] = mu         # set initial price to the mean reversion level

    # Generate price series using the OU process
    for i in range(1, N):
        dx = theta * (mu - x[i-1]) * dt + sigma * np.sqrt(dt) * np.random.normal()
        x[i] = x[i-1] + dx

    return pd.Series(x) * 100