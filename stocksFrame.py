from tkinter import *

class StocksFrame:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.buttonList = []
        self.frame = Frame(root)
        self.frame.pack(side=LEFT, anchor=NW)
    
    def assembleFrame(self):
        # Get the data from the model
        for key, value in self.model.getStockDict().items():
            button = Button(self.frame, text=key + " : " + str(value))
            self.buttonList.append(button)
            button.pack()


    
