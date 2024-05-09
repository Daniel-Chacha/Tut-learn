# rainbow
import turtle as t 
t.pensize(30)
t.speed(50)
t.bgcolor('white')

rainbow=['red','yellow','green','blue','indigo','violet']
t.penup()
t.setpos(0,-180)
t.pendown()
size=200

for x in rainbow:
    t.pencolor(x)
    t.fillcolor(x)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    size-=20

t.done()