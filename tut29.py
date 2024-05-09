#rectangles inside a bigger rectangle
import turtle as t 

t.speed(50)
t.pensize(5)

def drawrectangle(length,width):
    for x in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        length-=10
        width-=10

length=300
width=150

for i in range(8):
    drawrectangle(length,width)
    length-=20
    width-=20

t.ht()
t.done()