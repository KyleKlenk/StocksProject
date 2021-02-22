class Controller:
    def __init__(self, model):
        self.model = model
    
    def onBuyClick(self, tickerSymbol, buyPrice):
        self.model.buyStock(tickerSymbol, buyPrice)

    def onSellClick(self, tickerSymbol, sellPrice):
        self.model.sellStock(tickerSymbol, sellPrice)
