import turtle

a=int(input('Enter the length of the rectangle: '))
b=int(input('Enter the width of the rectangle: '))

t=turtle.Turtle()
t.speed(4)
t.pensize(6)
t.pencolor('red')

t.penup()
t.setpos(-50,50)
t.pendown()

for x in range(2):
    t.forward(a)
    t.right(90)

    t.forward(b)
    t.right(90)

turtle.done()