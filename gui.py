'''
Created on Jun 22, 2015

@author: william
'''
from tkinter import *
from tkinter import ttk
from RedditNewsAggregator import FindPosts

import praw

user_agent = "linux:PostAggregatorTest:v0.1 (by /u/Fillchiam)"
r = praw.Reddit(user_agent=user_agent)
submissions = r.get_subreddit('news').get_hot(limit=5)

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