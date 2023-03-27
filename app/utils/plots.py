import plotly.graph_objects as go
import pandas as pd

def performance_plot(performance):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=performance.index, y=performance)
    )

    fig.show()

def strategy_plot(data,periods):

    price = data["Price"]
    sma = data["Price"].rolling(periods).mean()
    smsd = data["Price"].rolling(periods).std()

    upper_band = sma + smsd*2
    lower_band = sma -  smsd*2
    long = pd.Series([x if y == 1 else None for (x,y) in zip(data['Price'],data['Trade'])])
    short = pd.Series([x if y == -1 else None for (x,y) in zip(data['Price'],data['Trade'])])
    
    stop_long = pd.Series([x if y == 2 else None for (x,y) in zip(data['Price'],data['Trade'])])
    stop_short = pd.Series([x if y == -2 else None for (x,y) in zip(data['Price'],data['Trade'])])
    
    take_long = pd.Series([x if y == 3 else None for (x,y) in zip(data['Price'],data['Trade'])])
    take_short = pd.Series([x if y == -3 else None for (x,y) in zip(data['Price'],data['Trade'])])
    
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=price.index,y=price,line=dict(color="#5D6D7E"),name="Price")
    )

    fig.add_trace(
        go.Scatter(x=sma.index,y=sma,line=dict(color="#E74C3C"),name="SMA")
    )

    fig.add_trace(
        go.Scatter(x=upper_band.index, y=upper_band, line=dict(color="#5DADE2"),showlegend=False)
    )

    fig.add_trace(
        go.Scatter(x=lower_band.index, y=lower_band, line=dict(color="#5DADE2"),showlegend=False)
    )

    fig.add_trace(
        go.Scatter(x=long.index, y=long,mode='markers',
                    marker_symbol=5,marker_color="green",marker_size=8,marker_line_color="green",name="Buy")
    )

    fig.add_trace(
        go.Scatter(x=short.index, y=short,mode='markers',
                    marker_symbol=6,marker_color="red",marker_size=8,marker_line_color="red",name="Sell")
    )

    fig.add_trace(
        go.Scatter(x=stop_long.index, y=stop_long,mode='markers',
                    marker_symbol=41,marker_color="orange",marker_size=8,
                    marker_line_color="orange",marker_line_width=2,name="stop long")
    )

    fig.add_trace(
        go.Scatter(x=stop_short.index, y=stop_short,mode='markers',
                    marker_symbol=41,marker_color="blue",marker_size=8,
                    marker_line_color="blue",marker_line_width=2,name="stop short")
    )

    fig.add_trace(
        go.Scatter(x=take_long.index, y=take_long,mode='markers',
                    marker_symbol=33,marker_color="orange",marker_size=8,
                    marker_line_color="orange",marker_line_width=2,name="take long")
    )

    fig.add_trace(
        go.Scatter(x=take_short.index, y=take_short,mode='markers',
                    marker_symbol=33,marker_color="blue",marker_size=8,
                    marker_line_color="blue",marker_line_width=2,name="take short")
    )

    fig.show()