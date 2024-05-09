#a moving square
import turtle as t 

t.speed('fastest')
t.penup()
t.goto(-260,-250)
t.pendown()

t.tracer(n=None)

def square(s):
    for x in range(4):
        t.fd(s)
        t.lt(90)

def draw(z):
    t.clear()

    for i in range(z):
        square(70)
        t.fd(70)


draw(10)
t.done()