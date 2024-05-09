#undo a square
import turtle


turtle.up()
turtle.setpos(-50,50)
turtle.down()

for x in range(4):
    turtle.forward(100)
    turtle.right(90)

for x in range(8):
    turtle.undo()
turtle.done()