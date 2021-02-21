import tkinter as tk
import apiTest as aT

def main():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    tickersList = []
    widgetList = []
    dataframeDictionary = {}

    tickersList = aT.addStockTicker("SNC.TO", tickersList)
    tickersList = aT.addStockTicker("HIVE.V", tickersList)
    dataframeDictionary = aT.getStockPrices(dataframeDictionary, tickersList)
    for key, value in dataframeDictionary.items():
        tk.Label(root, text=key + " : " + str(value))
    

    for c in sorted(root.children):
        root.children[c].pack()
    root.mainloop()

main()