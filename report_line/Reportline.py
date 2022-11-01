import os 
from tkinter import *
import csv

from utils import timer


class ui(Frame):
    def __init__(self,master):
        self.master = master
        super().__init__(self.master)
        self.Timer = timer.timer()
        
        Button(self,text="start",command = self.start).grid(row = 0,column = 0)
        Button(self,text="stop",command = self.end).grid(row = 1,column = 0)
        Button(self,text="get",command = self.refleshtimer).grid(row = 2,column = 0)
    def start(self):
        self.Timer.start()
    def end(self):
        self.Timer.end()
    def refleshtimer(self):
        print(self.Timer.getdata())
        

class lineconect:
    def __init__(self):
        self.text = ""
        print("test")

if __name__ == '__main__':
    root = Tk()
    root.title("test")
    Ui = ui(root)
    Ui.grid(row = 1,column = 1)
    root.mainloop()
