# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 05:52:11 2024

@author: Eshaan Gurjar
"""

from tkinter import *
import random
root = Tk()
root.title("Random Number List")
root.geometry("400x400")


items = []
text = Entry(root)
L1 = Label(root)
L2 = Label(root)

def generator():
    L2["text"] += "⠀"
    maxop = len(items)
    packNum = random.randint(1,maxop)
    L2["text"] += "pack item " + str(packNum)

def addItem():
    item = text.get()
    items.append(item)
    L1["text"] = items
    
btn = Button(root, text = "Generate Number", command = generator)
pack = Button(root, text = "Add item to list", command = addItem)

L1.place(relx = 0.5, rely = 0.6, anchor = CENTER)
L2.place(relx = 0.5, rely = 0.7, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
text.place(relx = 0.5, rely = 0.3, anchor = CENTER)
pack.place(relx = 0.5, rely = 0.4, anchor = CENTER)


root.mainloop()