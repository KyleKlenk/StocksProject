import datetime as dt
import pandas as pd
import pandas_datareader.data as web

class Model:
    def __init__(self):
        # Instance Variables
        self.stockList = []
        self.stockDict = {}
        self.stockeTickerObjects = []
        self.todaysDate = dt.datetime(dt.date.today().year, 
                        dt.date.today().month, 
                        dt.date.today().day)
            

    def addStockTicker(self, ticker):
        self.stockList.append(ticker)
        self.assembleDict()
    
    def removeStockTicker(self, ticker):
        self.stockList.remove(ticker)
        del self.stockDict[ticker]
    
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
    


    
