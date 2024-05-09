#multiple circles
import turtle

turtle.speed(20)
turtle.color('black')
turtle.pensize(4)

def draw(rad):
    turtle.circle(rad)

    turtle.up()
    turtle.setpos(0,-rad)
    turtle.down()

for x in range(5):
    draw(40*x)

turtle.done()