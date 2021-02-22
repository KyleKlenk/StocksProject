# This class will create the stock ticker object
class StockTicker:
    def __init__(self, stockTicker, stockPrice, buyPrice, pricePercentage):
        self.stockTicker = stockTicker
        self.stockPrice = stockPrice
        self.buyPrice = buyPrice
        self.pricePercentage = pricePercentage
    
    def getStockTicker(self):
        return self.stockTicker
    
    def getStockPrice(self):
        return self.stockPrice
    
    def setStockPrice(self, stockPrice):
        self.stockPrice = stockPrice
    
    def getBuyPrice(self):
        return self.buyPrice
    
    def setBuyPrice(self, buyPrice):
        self.buyPrice = buyPrice
    
    def getPricePercentage(self):
        return self.pricePercentage
    
    def setPricePercentage(self, percentage):
        self.pricePercentage = percentage

