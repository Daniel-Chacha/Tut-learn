#hexagon
import turtle as t

t.speed(10)
t.pensize(6)

t.penup()
t.goto(-20,50)
t.pendown()
for x in range(6):
    t.fd(100)
    t.rt(60)

t.done()