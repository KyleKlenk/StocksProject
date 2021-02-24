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
    
    """
    This will be the function that carries out the buy and sell rules
    """
    def analyzePortfolio(self):
        # if the percentage is below -6.5%
        if (self.pricePercentage <= -6.5):
            # send text message sell
            # log our recomendation
            print(self.stockTicker, "sell")
        
        # else if percentage is above 20%
        elif (self.pricePercentage >= 20):
            # send text message you may want to think about selling
            # log our recomendation
            print(self.stockTicker, "Think about selling")
        else:
            # log some key stats about ourselves
            print(self.stockTicker, "Log")


