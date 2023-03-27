import numpy as np
import pandas as pd

def mappingTrades(x):
    if (x==2) or (x==3):
        return -1
    elif (x==-2) or (x==-3):
        return 1
    else:
        return x

def strategyPerfomance(data):
    price = data["Price"]
    trades = data["Trade"].apply(lambda x: mappingTrades(x))
    returns = data["Price"].pct_change().fillna(0) * data["Trade"]

    init_value = 1000
    portfolio_value = init_value

    shares = []
    for px,pos,ret in zip(price,trades,returns):
        share =  (portfolio_value/px) * pos * -1
        portfolio_value = portfolio_value *(1+ret)
        shares.append(share)

    cumulative_returns = np.cumprod(1 + returns).dropna()
    annualized_returns = (cumulative_returns.iloc[-1]**(252/len(returns))-1)*100

    Drawdown = cumulative_returns - np.maximum.accumulate(cumulative_returns)
    Max_drawdown = Drawdown.min()

    count_profits = pd.Series([i for i in returns if i > 0]).count()
    count_losses = pd.Series([i for i in returns if i < 0]).count()
    mean_profits = pd.Series([i for i in returns if i > 0]).mean()
    mean_losses = pd.Series([i for i in returns if i < 0]).mean()
    

    print(f"""
        Backtesting performance
        -----------------------
        Cummulative returns:
        {cumulative_returns.iloc[-1]:.2%}

        Annualized returns:
        {annualized_returns:.2%}

        Max DrawDon:
        {Max_drawdown:.2}

        P&L after investing $1,000:
        {portfolio_value:,}

        signals performance:
        ----------------------
        |       | Profits | Losses
        |Count  |{count_profits}      | {count_losses}
        |Mean   |{mean_profits:.2%}    | {mean_losses:.2%}
        ----------------------
        Ratio : {np.abs(mean_profits/mean_losses):.2}:1
    """)

    return cumulative_returns



    

