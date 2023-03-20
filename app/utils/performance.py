import numpy as np
import pandas as pd
def strategyPerfomance(data):
    price = data["Price"]
    trades = data["Trade"]
    returns = data["Price"].pct_change().fillna(0) * data["Trade"]

    init_value = 1000
    portfolio_value = init_value

    shares = []
    for px,pos,ret in zip(price,trades,returns):
        share =  (portfolio_value/px) * pos * -1
        portfolio_value = portfolio_value *(1+ret)
        shares.append(share)

    cumulative_returns = np.cumprod(1 + returns)
    annualized_returns = (cumulative_returns.iloc[-1]**(252/len(returns))-1)*100
    sharpe_ratio = np.sqrt(252) * (returns.mean()-0.07) / returns.std()
    max_cumulative = np.maximum.accumulate(cumulative_returns.dropna())
    max_cumulative = pd.Series([1 if i <1 else i for i in max_cumulative])
    Drawdown = (cumulative_returns/max_cumulative)-1
    Max_drawdown = Drawdown.min() * 100
    
    print(f"""
        Backtesting performance
        -----------------------
        Cummulative returns:
        {cumulative_returns.iloc[-1]}

        Annualized returns:
        {annualized_returns}

        Sharpe Ratio:
        {sharpe_ratio}

        Max DrawDon:
        {Max_drawdown}

        P&L:
        {portfolio_value}
    """)

    return cumulative_returns



    

