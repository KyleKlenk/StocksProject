class Controller:
    def __init__(self, model):
        self.model = model
    
    def onBuyClick(self, tickerSymbol, buyPrice):
        print(tickerSymbol)
        print(buyPrice)

    def onSellClick(self, tickerSymbol, sellPrice):
        print(tickerSymbol)
        print(sellPrice)
