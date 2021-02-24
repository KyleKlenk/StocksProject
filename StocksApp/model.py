import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from stockTicker import *


class Model:
    def __init__(self, database):
        self.database = database
        # Instance Variables
        self.stockList = []
        self.stockTickerObjects = []
        self.todaysDate = dt.datetime(dt.date.today().year, 
                        dt.date.today().month, 
                        dt.date.today().day)
        self.mainOb = None
        
    """
    This is my makeshift listener. It calls "main object" which runs the program which then
    calls the correct frames to update.
    """
    def setMain(self, mainOb):
        self.mainOb = mainOb

    def buyStock(self, tickerSymbol, buyPrice):
        tickerSymbol = tickerSymbol
        buyPrice = round(float(buyPrice), 2)
        currentPrice = self.getCurrentStockPrice(tickerSymbol)
        percentage = round(((currentPrice - buyPrice) / buyPrice) * 100, 2)
        
        stockTicker = StockTicker(tickerSymbol, currentPrice, buyPrice, percentage)
        self.stockTickerObjects.append(stockTicker)
        self.modelUpdated()
    
    def modelUpdated(self):
        self.mainOb.modelUpdated()

    def updateStocks(self):
        for stockTicker in self.stockTickerObjects:
            df = web.DataReader(stockTicker.getStockTicker(), 'yahoo', self.todaysDate, self.todaysDate)
            price = df.iloc[0]["Close"]
            stockTicker.setStockPrice(round(price, 2))
            stockTicker.setPricePercentage(round(
                ((price - stockTicker.getBuyPrice()) / stockTicker.getBuyPrice()) * 100, 2))
        self.modelUpdated()

    
    def getStockTickerObjects(self):
        return self.stockTickerObjects
    
    def sellStock(self, tickerSymbol, sellPrice):
        print(tickerSymbol)
        print(sellPrice)
    
    
    def getCurrentStockPrice(self, ticker):
        df = web.DataReader(ticker, 'yahoo', self.todaysDate, self.todaysDate)
        price = df.iloc[0]["Close"]
        return round(price, 2)
    

    


    
