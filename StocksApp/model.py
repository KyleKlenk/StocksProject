import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from stockTicker import *
from databaseModel import *


class Model:
    def __init__(self):
        self.database = DatabaseModel()
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
        self.database.insertPurchace(tickerSymbol, buyPrice)
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
            stockTicker.analyzePortfolio()
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

    def getStocksFromDatabase(self):
        rows = self.database.selectAllPurchaces()
        # create the stockTicker objects and notify the view
        for row in rows:
            tickerSymbol = row[1]
            buyPrice = row[2]
            currentPrice = 0 # will be updated in 5 seconds
            percentage = 0 # will also be updated in 5 seconds
            ticker = StockTicker(tickerSymbol, currentPrice, buyPrice, percentage)
            self.stockTickerObjects.append(ticker)
        self.modelUpdated()
        




    

    


    
