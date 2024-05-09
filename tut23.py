#a unique 'star' shaped pattern
import turtle as t 

t.speed(50)
dist=1
flag=500

while flag:
    t.fd(dist)
    t.left(200)
    t.left(1)
    dist+=1
    flag-=1

t.done()