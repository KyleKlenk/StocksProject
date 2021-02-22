from tkinter import *
from model import *
from stocksFrame import *
from buyRemoveFrame import *
from controller import *

class Main:
    def __init__(self, model, controller):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title("Stocks Application")
        self.model = model
        self.controller = controller
        self.stocksFrame = StocksFrame(self.root, self.model)
        self.buyFrame = BuyFrame(self.root, self.model, self.controller)
        self.sellFrame = SellFrame(self.root, self.model, self.controller)

    def run(self):
        self.root.mainloop()

model = Model()
controllerObject = Controller(model)
model.addStockTicker("SNC.TO")
main = Main(model, controllerObject)
main.run()

