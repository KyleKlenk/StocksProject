from tkinter import *
from model import *
from stocksFrame import *
from buySellFrame import *
from controller import *
from databaseModel import *

class Main:
    def __init__(self, model, controller):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title("Stocks Application")
        self.model = model
        model.setMain(self)
        self.controller = controller
        self.stocksFrame = StocksFrame(self.root, self.model)
        self.buyFrame = BuyFrame(self.root, self.model, self.controller)
        self.sellFrame = SellFrame(self.root, self.model, self.controller)

    def run(self):
        self.model.getStocksFromDatabase()
        self.root.after(10000, self.updateTask)
        self.root.mainloop()
    
    def modelUpdated(self):
        self.stocksFrame.update()
    
    def updateTask(self):
        self.model.updateStocks()
        self.root.after(10000, self.updateTask)


model = Model()
controllerObject = Controller(model)
main = Main(model, controllerObject)
main.run()

