from tkinter import *
from model import *
from stocksFrame import *
from buySellFrame import *
from controller import *
from databaseModel import *
from thespian.actors import *

class Main(Actor):
    def receiveMessage(self, msg, sender):
        if msg == "Start":
            self.root = Tk()
            self.root.geometry("1920x1080")
            self.root.title("Stocks Application")

            # create the model and set main
            self.model = Model()
            self.model.setMain(self)
            self.controller = Controller(self.model)
            self.stocksFrame = StocksFrame(self.root, self.model)
            self.buyFrame = BuyFrame(self.root, self.model, self.controller)
            self.sellFrame = SellFrame(self.root, self.model, self.controller)
            self.run()
        
        else:
            print("unknown message")

    def run(self):
        self.model.getStocksFromDatabase()
        self.root.after(10000, self.updateTask)
        self.root.mainloop()
    
    def modelUpdated(self):
        self.stocksFrame.update()
    
    def updateTask(self):
        self.model.updateStocks()
        self.root.after(10000, self.updateTask)


if __name__ == "__main__":

    # This may mean create actor then tell myself to start
    main = ActorSystem().createActor(Main)
    print("starting")
    ActorSystem().tell(main, "Start")

# model = Model()
# controllerObject = Controller(model)
# main = Main(model, controllerObject)
# main.run()

