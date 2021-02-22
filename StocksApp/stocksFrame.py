from tkinter import *
from stockTicker import *

class StocksFrame:
    def __init__(self, root, model):
        # variables for model and root paramaters
        self.root = root
        self.model = model
        # create the frame and place it inside its parent aka root
        self.frame = Frame(root)
        self.frame.pack(side=LEFT, anchor=NW)
        # Labels to create a list of owned stocks
        self.stockTickerLabel = Label(self.frame, text="Stock Ticker :")
        self.stockTickerLabel.grid(row=0, column=0)
        self.currentPriceLabel = Label(self.frame, text="Current Price :")
        self.currentPriceLabel.grid(row=0, column=1)
        self.boughtPriceLabel = Label(self.frame, text="Purchase Price :")
        self.boughtPriceLabel.grid(row=0, column=2)
        self.pricePercentage = Label(self.frame, text="%")
        self.pricePercentage.grid(row=0, column=3)
        
        # Variables for list of stocks
        self.buttonList = []
        
    def update(self):
        stockTickerList = self.model.getStockTickerObjects()
        rowCounter = 1
        for stockTicker in stockTickerList:
            Label(self.frame, text=stockTicker.getStockTicker()).grid(row=rowCounter)
            Label(self.frame, text=stockTicker.getStockPrice()).grid(row=rowCounter, column=1)
            Label(self.frame, text=stockTicker.getBuyPrice()).grid(row=rowCounter, column=2)
            Label(self.frame, text=stockTicker.getPricePercentage()).grid(row=rowCounter, column=3)
            rowCounter += 1
            
    
    def assembleFrame(self):
        # Get the data from the model

        for key, value in self.model.getStockDict().items():
            button = Button(self.frame, text=key + " : " + str(value))
            self.buttonList.append(button)
            button.pack()


    
