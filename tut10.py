#a spiderweb
import turtle as t

t.setup(700,600)
t.bgcolor('black')
t.speed(40)
t.pensize(6)
t.pencolor('red')

side=5

for  x in range(6):
    t.forward(250)
    t.backward(250)
    t.right(60)

for x in range(8):
    t.penup()
    t.setpos(0,0)
    t.pendown()
    t.setheading(0)
    t.forward(side)
    t.right(120)

    for j in range(6):
        t.forward(side+2)
        t.right(60)
        side+=5


t.done()