import sqlite3 as sql

class DatabaseModel:
    def __init__(self):
        self.conn = sql.connect("stocks.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM PurchaseTable")
        self.rows = self.c.fetchall()
        for row in self.rows:
            print(row)
