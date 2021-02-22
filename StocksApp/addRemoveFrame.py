from tkinter import *


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
