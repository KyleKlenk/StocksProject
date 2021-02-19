import apiTest as at

## TestDataStrucutre
myPortfolioTickers = []


## Testing addStockTicker
myPortfolioTickers = at.addStockTicker("SNC.TO", myPortfolioTickers)
print(myPortfolioTickers)
myPortfolioTickers = at.addStockTicker("APPL", myPortfolioTickers)
print(myPortfolioTickers)
myPortfolioTickers = at.addStockTicker("BITK.V", myPortfolioTickers)
print(myPortfolioTickers)
myPortfolioTickers = at.addStockTicker("ATZ.TO", myPortfolioTickers)
print(myPortfolioTickers)

## Testing removeStockTicker
myPortfolioTickers = at.removeStockTicker("SNC.TO", myPortfolioTickers)
print(myPortfolioTickers)
myPortfolioTickers = at.removeStockTicker("APPL", myPortfolioTickers)
print(myPortfolioTickers)
myPortfolioTickers = at.removeStockTicker("BITK.V", myPortfolioTickers)
print(myPortfolioTickers)
myPortfolioTickers = at.removeStockTicker("ATZ.TO", myPortfolioTickers)
print(myPortfolioTickers)