from tkinter import *

class BuyFrame:
    def __init__(self, root, model, controller):
        self.root = root
        self.model = model
        self.controller = controller
        self.frame = Frame(root)
        self.frame.pack(side=LEFT, anchor=N)

        self.buyLabelTitle = Label(self.frame, text="Buy Stock")
        self.buyLabelTitle.grid(row=0, column=1)
        self.tickerSymbolLabel = Label(self.frame, text="Ticker Symbol: ")
        self.tickerSymbolLabel.grid(row=1, column=0)
        self.tickerSymbolInput = Entry(self.frame)
        self.tickerSymbolInput.grid(row=1, column=1)
        self.buyPriceLabel = Label(self.frame, text="Buy Price: ")
        self.buyPriceLabel.grid(row=2, column=0)
        self.buyPriceInput = Entry(self.frame)
        self.buyPriceInput.grid(row=3, column=1)
        self.buyButton = Button(self.frame, text="Buy")
        self.buyButton.grid(row=4, column=1)
        
class SellFrame:
    def __init__(self, root, model, controller):
        self.root = root
        self.model = model
        self.controller = controller
        self.frame = Frame(root)
        self.frame.pack(side=LEFT, anchor=N)

        self.sellLabelTitle = Label(self.frame, text="Sell Stock")
        self.sellLabelTitle.grid(row=0, column=1)
        self.tickerSymbolLabel = Label(self.frame, text="Ticker Symbol: ")
        self.tickerSymbolLabel.grid(row=1, column=0)
        self.tickerSymbolInput = Entry(self.frame)
        self.tickerSymbolInput.grid(row=1, column=1)
        self.sellPriceLabel = Label(self.frame, text="sell Price: ")
        self.sellPriceLabel.grid(row=2, column=0)
        self.sellPriceInput = Entry(self.frame)
        self.sellPriceInput.grid(row=3, column=1)
        self.sellButton = Button(self.frame, text="Sell")
        self.sellButton.grid(row=4, column=1)

class AddRemoveFrame:
    def __init__(self, root, model, controller):
        self.root = root
        self.model = model
        self.controller = controller
        self.frame = Frame(root)
        self.frame.pack(side=LEFT, anchor=N)

        self.label = Label(self.frame, text="Ticker Symbol")

        self.inputText = Entry(self.frame)
        self.addButton = Button(self.frame, text="Add", 
        command=self.buttonClick)

        self.label.grid(row=0)
        self.inputText.grid(row=0, column=1)
        self.addButton.grid(row=1)
    
    def buttonClick(self):
        self.controller.addTickerClick(self.inputText.get())


    
    # def assembleFrame(self):
    #     .grid(row=0)
    #     inputText = Entry(self.frame)
    #     inputText.grid(row=0, column=1)
