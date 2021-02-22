from tkinter import *
import apiTest as aT

def main():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Stocks Application")
    frame = Frame(root)
    frame.pack()

    tickersList = []
    buttonList = []
    dataframeDictionary = {}

    tickersList = aT.addStockTicker("SNC.TO", tickersList)
    tickersList = aT.addStockTicker("HIVE.V", tickersList)
    dataframeDictionary = aT.getStockPrices(dataframeDictionary, tickersList)
    for key, value in dataframeDictionary.items():
        button = Button(frame, text=key + " : " + str(value))
        buttonList.append(button)
        button.pack()
    
    root.mainloop()

main()