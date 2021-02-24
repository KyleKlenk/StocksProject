from thespian.actors import *
from tkinter import *
 
class GUI(Actor):
    def receiveMessage(self, message, sender):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title("Stocks Application")
        self.root.mainloop()
        
 
if __name__ == "__main__":
    gui = ActorSystem().createActor(GUI)
    ActorSystem().tell(gui, "Start")