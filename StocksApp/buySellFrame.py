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
        self.buyPriceInput.grid(row=2, column=1)
        self.buyButton = Button(self.frame, text="Buy", command=self.buttonClick)
        self.buyButton.grid(row=3, column=1)

    def buttonClick(self):
        self.controller.onBuyClick(self.tickerSymbolInput.get(), 
                                        self.buyPriceInput.get())
        self.tickerSymbolInput.delete(0, 'end')
        self.buyPriceInput.delete(0, 'end')
        
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
        self.sellPriceInput.grid(row=2, column=1)
        self.sellButton = Button(self.frame, text="Sell", command=self.buttonClick)
        self.sellButton.grid(row=3, column=1)

    def buttonClick(self):
        self.controller.onSellClick(self.tickerSymbolInput.get(),
                                          self.sellPriceInput.get())
        self.tickerSymbolInput.delete(0, "end")
        self.sellPriceInput.delete(0, "end")
        


