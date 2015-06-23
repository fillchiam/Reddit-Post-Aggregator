'''
Created on Jun 20, 2015

@author: william
'''
import praw

user_agent = "linux:PostAggregatorTest:v0.1 (by /u/Fillchiam)"
r = praw.Reddit(user_agent=user_agent)
submissions = r.get_subreddit('news').get_hot(limit=30)
resultlist = []
def lister():
    for x in submissions:
        result = (str(x))
        resultlist.append(result)
        
lister()