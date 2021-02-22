import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
### Global Variables ###
todaysDate = dt.datetime(dt.date.today().year, 
                        dt.date.today().month, 
                        dt.date.today().day)

"""
Input: TickerSymbol and TickerContainerStructure
Output: TickerContainer with new TickerSymbol
"""
def addStockTicker(ticker, tickerSymbolsList):
    tickerSymbolsList.append(ticker)
    return tickerSymbolsList

"""
Input: TickerSymbol and TickerContainerStructure
Output: TickerContainer without TickerSymbol
"""
def removeStockTicker(ticker, tickerSymbolsList):
    tickerSymbolsList.remove(ticker)
    return tickerSymbolsList

"""
Input: dictionary to hold the key value pairs
Key = Ticker Symbol
Value = DataFrame object
"""
def getStockPrices(dataStructure, tickerSymbolsList):
# date will be an error when stock market is not open
    for ticker in tickerSymbolsList:
        df = web.DataReader(ticker, 'yahoo', dt.datetime(dt.date.today().year, dt.date.today().month, dt.date.today().day - 2), 
        dt.datetime(dt.date.today().year, dt.date.today().month, dt.date.today().day - 2))
        column = df.iloc[0]["Close"]
        print(column)
        dataStructure[ticker] = column
    return dataStructure


def main():
    myPortfolioTickers = []
    myDataframes = {}

    myPortfolioTickers = addStockTicker("SNC.TO", myPortfolioTickers)
    myDataFrames = getStockPrices(myDataframes, myPortfolioTickers)

    



# while(1):
#      df = web.DataReader('SNC.TO', 'yahoo', todaysDate, todaysDate)
#      print(df.head())
#      time.sleep(60)

