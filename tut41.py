#ontimer() ; is a function that is used to schedule a function to be called after a specified amount of time. 
import turtle as t 
import random

col = ['red', 'yellow', 'green', 'blue', 
       'white', 'black', 'orange', 'pink'] 

def fxn():
    
    x=random.randint(0,7)
    t.bgcolor(col[x])

for i in range(10):
    t.ontimer(fxn,i*400)


t.done()