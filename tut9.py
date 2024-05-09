#a solid cube filled with colour
import turtle as t 

t.speed(10)

#front side
t.penup()
t.goto(50,-40)
t.pendown()
t.fillcolor('black')
t.begin_fill()
for x in range(4):
    t.fd(150)
    t.lt(90)
t.end_fill()

#left side
t.fillcolor('blue')
t.begin_fill()
t.lt(150)
t.fd(150)
t.rt(60)
t.fd(150)
t.rt(120)
t.fd(150)
t.end_fill()

#top
t.setheading(0)
t.fd(150)
t.fillcolor('red')
t.begin_fill()
t.lt(150)
t.fd(150)
t.lt(30)
t.fd(150)
t.lt(150)
t.fd(150)
t.end_fill()

t.ht()
t.done()