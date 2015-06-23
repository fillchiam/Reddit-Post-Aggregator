'''
Created on Jun 22, 2015

@author: william
'''
from tkinter import *
from tkinter import ttk
from RedditNewsAggregator import FindPosts

root = Tk()
root.title("Reddit Post Aggregator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


FindPosts.lister()

for item in FindPosts.resultlist:
    print(item)

root.mainloop()
