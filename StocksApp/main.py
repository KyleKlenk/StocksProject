from tkinter import *
from model import *
from stocksFrame import *
from addRemoveFrame import *
from controller import *

class Main:
    def __init__(self, model, controller):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title("Stocks Application")
        self.model = model
        self.controller = controller
        self.StocksFrame = StocksFrame(self.root, self.model)
        self.StocksFrame.assembleFrame()
        self.AddRemoveFrame = AddRemoveFrame(self.root, self.model, self.controller)

    def run(self):
        
        
        self.root.mainloop()

model = Model()
controllerObject = Controller(model)
model.addStockTicker("SNC.TO")
main = Main(model, controllerObject)
main.run()

