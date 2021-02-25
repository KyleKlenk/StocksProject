class StockTicker(object):
    def __init__(self, ticker, buyPrice, currentPrice, percentage):
        self.ticker = ticker
        self.buyPrice = buyPrice
        self.currentPrice = currentPrice
        self.percentage = percentage
