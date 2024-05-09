#octagon
import turtle as t
 
t.pensize(5)
t.pencolor('red')

t.penup()
t.setpos(-50,50)
t.pendown()
for x in range(8):
    t.fd(100)
    t.right(45)

t.done()