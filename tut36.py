#clock
import turtle as t 

t.pensize(4)

val=0
for i in range(12):
    val+=1
    t.penup()    
    t.home()                # move turtle in air
    t.setheading(-30*(i+3)+75)    #  for circular motion
    t.forward(22)                # move forward for space
    t.pendown()                  # move turtle to surface
    t.fd(50)                     # move forward for dash line
    t.penup()                     # move turtle in air
    t.fd(20)                     # move forward for space

    #write clock integer
    t.write(str(val),align='center',font=('Arial',12,'normal'))

t.done()