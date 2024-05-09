#concetric circles,with same centre
import turtle as t 
t.speed(50)

r=10

for i in range(20):
    t.circle(r*i)
    t.penup()
    t.sety((r*i)*(-1)) #The multiplication by -1 ensures that the turtle moves downward along the y-axis. The sety function sets the y-coordinate without changing the x-coordinate.
    t.pendown()

t.done()
