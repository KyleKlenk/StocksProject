-- SQLite
CREATE TABLE PurchaseTable(
    purchaseID INTEGER PRIMARY KEY,
    tickerSymbol TEXT NOT NULL,
    buyPrice REAL NOT NULL
);