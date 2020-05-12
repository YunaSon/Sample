from tkinter import *

#1. Make Window

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill = BOTH, expand=1)
        quitButton = Button(self, text="Quit")
        quitButton.place(x=0, y=0)


root = Tk()
root.geometry("400 * 300")
app = Window(root)
root.mainloop()
