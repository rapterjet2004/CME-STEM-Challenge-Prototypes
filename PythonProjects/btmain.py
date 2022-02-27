import backtrader as bt
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from strategies import *

#Instantiate Cerebro engin
cerebro = bt.Cerebro()

#Add data feed to Cerebro
data = bt.feeds.GenericCSVData(
    dataname=r'C:\Users\juliu\PythonProjects\BTC_3.csv',
    fromdate=datetime.datetime(2018, 1, 1),
    todate=datetime.datetime(2022, 1, 1),
    nullvalue=0.0,
    dtformat=('%m/%d/%Y'),
    datetime=0,
    high=3,
    low=4,
    open=2,
    close=2,
    volume=8,
    openinterest=-1,
    timeframe=bt.TimeFrame.Days)

data1 = bt.feeds.YahooFinanceCSVData(
    dataname=r'C:\Users\juliu\PythonProjects\GME.csv',
    fromdate=datetime.datetime(2018, 1, 1),
    todate=datetime.datetime(2022, 1, 1),
)

cerebro.adddata(data)

#Add strategy to Cerebro
cerebro.addstrategy(PrintClose)

cerebro.addsizer(bt.sizers.SizerFix, stake=3)
if __name__ == '__main__':
    # Run Cerebro Engine
    start_portfolio_value = cerebro.broker.getvalue()

    cerebro.run(runonce=False) 
    #print('matplotlib: {}'. format(matplotlib. __version__))
    

    end_portfolio_value = cerebro.broker.getvalue()
    pnl = end_portfolio_value - start_portfolio_value
    print(f'Starting Portfolio Value: {start_portfolio_value:2f}')
    print(f'Final Portfolio Value: {end_portfolio_value:2f}')
    print(f'PnL: {pnl:.2f}')

    cerebro.plot()