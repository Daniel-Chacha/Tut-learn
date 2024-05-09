#triangles inside another triangle
import turtle as t 

def triangle(side):
    for i in range(3):
        t.fd(side)
        t.lt(120)
        side-=10

side=300
for x in range(10):
    triangle(side)
    side-=30

t.done()