#cube
import turtle
tut=turtle.Screen()
tut.bgcolor('green')

t=turtle.Turtle()
t.speed(10)
t.pensize(4)
t.pencolor('red')

for x in range(4):
    t.forward(100)
    t.left(90)

t.goto(50,50)

for x in range(4):
    t.forward(100)
    t.left(90)

t.goto(150,50)
t.goto(100,0)

t.goto(100,100)
t.goto(150,150)

t.goto(50,150) 
t.goto(0,100)
turtle.done()