import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from stockTicker import *


class Model:
    def __init__(self):
        # Instance Variables
        self.stockList = []
        self.stockDict = {}
        self.stockTickerObjects = []
        self.todaysDate = dt.datetime(dt.date.today().year, 
                        dt.date.today().month, 
                        dt.date.today().day)
        self.mainOb = None
        
    def setMain(self, mainOb):
        self.mainOb = mainOb

    def addStockTicker(self, ticker):
        self.stockList.append(ticker)
        self.assembleDict()

    def buyStock(self, tickerSymbol, buyPrice):
        tickerSymbol = tickerSymbol
        buyPrice = round(float(buyPrice), 2)
        currentPrice = round(self.getCurrentStockPrice(tickerSymbol), 2)
        percentage = round(((currentPrice - buyPrice) / buyPrice) * 100, 2)
        
        stockTicker = StockTicker(tickerSymbol, currentPrice, buyPrice, percentage)
        self.stockTickerObjects.append(stockTicker)
        self.modelUpdated()
    
    def modelUpdated(self):
        self.mainOb.modelUpdated()
    
    def getStockTickerObjects(self):
        return self.stockTickerObjects
    
    def sellStock(self, tickerSymbol, sellPrice):
        print(tickerSymbol)
        print(sellPrice)
    
    def removeStockTicker(self, ticker):
        self.stockList.remove(ticker)
        del self.stockDict[ticker]
    
    def getCurrentStockPrice(self, ticker):
        df = web.DataReader(ticker, 'yahoo', self.todaysDate, self.todaysDate)
        price = df.iloc[0]["Close"]
        return price

    
    def assembleDict(self):
        for ticker in self.stockList:
            df = web.DataReader(ticker, 'yahoo', self.todaysDate, self.todaysDate)
            closeColumn = df.iloc[0]["Close"]
            self.stockDict[ticker] = closeColumn
    
    def getStockDict(self):
        return self.stockDict

    

# model = Model()
# model.addStockTicker("SNC.TO")
# print(model.stockList)
# print(model.stockDict)
# model.removeStockTicker("SNC.TO")
# print(model.stockList)
# print(model.stockDict)
    


    
