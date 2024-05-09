#spiral pattern
import turtle as t 
t.speed(20)
t.bgcolor('white')

dist=1
flag=500

while flag:
    t.fd(dist)
    t.lt(120)
    t.lt(1)
    dist+=1
    flag-=1

t.done()