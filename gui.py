'''
Created on Jun 22, 2015

@author: william
'''
from tkinter import *
from tkinter import ttk
from RedditNewsAggregator import FindPosts

root = Tk()
root.title("Reddit Post Aggregator")
root.minsize(width=600, height=400)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

FindPosts.lister()

lbox = Listbox(mainframe, height=30)
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))

for item in FindPosts.resultlist:
    lbox.insert(END, item)
    print(item)

root.mainloop()
