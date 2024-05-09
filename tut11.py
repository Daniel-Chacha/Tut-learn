#sun with rays
import turtle as t
t.bgcolor('turquoise')
t.speed(40)
t.pensize(5)

#the rays
def therays(t,length,radius):
    for x in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length +radius)
        t.left(90)

#the sun
t.penup()
t.goto(85,120)
t.fillcolor('yellow')
t.pendown()
t.begin_fill()
t.circle(45)
t.end_fill()


t.penup()
t.goto(85,169)
t.pendown()
therays(t,85,54)
t.right(45)
therays(t,85,45)
t.left(45)

t.done()
