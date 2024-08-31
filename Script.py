#!/bin/python3

from tkinter import *
from tkinter.ttk import *
import subprocess
import os

def airplus(root):
    subprocess.Popen('dex "/home/noah/.local/share/applications/HabboAirPlus.desktop"', shell=True)
    root.destroy()

def wine(root):
    subprocess.run('xdg-open "bottles:run/Habbo/Habbo Launcher"', shell=True)
    root.destroy()

def website():
    os.system('kde-open "https://habbo.com/"')


root = Tk()
root.title("Habbo Launcher")
root.resizable(width=False, height=False)
frame = Frame(root,padding=10)
frame.grid()

Btn1 = Button(root, text="HabboAirPlus", command=lambda: airplus(root), width=40)
Btn1.grid(column=0,row=0)

Btn2 = Button(root, text="Wine", command=lambda: wine(root), width=40)
Btn2.grid(column=0,row=1)

Btn3 = Button(root, text="Website", command=lambda: website(), width=40)
Btn3.grid(column=0,row=2)

root.mainloop()
