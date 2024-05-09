#cuboid
import turtle

turtle.bgcolor('black')

turtle.pensize(5)
turtle.pencolor('green')
turtle.speed(10)

turtle.penup()
turtle.setposition(-50,-50)
turtle.pendown()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.setpos(60,80)
for x in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.goto(160,80)
turtle.goto(50,-50)

turtle.goto(50,50)
turtle.goto(160,180)

turtle.goto(60,180)
turtle.goto(-50,50)
turtle.done()
