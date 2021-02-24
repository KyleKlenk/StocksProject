import sqlite3 as sql

class DatabaseModel:
    def __init__(self):
        # This will create the database if it does not already exist
        self.conn = sql.connect("stocks.db")
        self.c = self.conn.cursor()
        self.conn.close()

        # Test execute
        # self.c.execute("SELECT * FROM PurchaseTable")
        # self.rows = self.c.fetchall()
        # for row in self.rows:
        #     print(row)
    
    def getConnection(self):
        self.conn = sql.connect("stocks.db")
        self.c = self.conn.cursor()
    
    def insertPurchace(self, tickerSymbol, buyPrice):
        self.getConnection()
        self.c.execute("INSERT INTO PurchaseTable (tickerSymbol, buyPrice) VALUES (?, ?)", 
        (tickerSymbol, buyPrice))
        self.conn.commit()
        self.conn.close()
    
    def selectAllPurchaces(self):
        self.getConnection()
        self.c.execute("SELECT * FROM PurchaseTable")
        rows = self.c.fetchall()
        self.conn.close()
        return rows