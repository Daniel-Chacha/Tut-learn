#clock
import turtle as t 

t.pensize(4)

val=0
for i in range(12):
    val+=1
    t.penup()                     # move turtle in air
    t.setheading(-30*(i+3)+75)    #  for circular motion
    t.forward(22)                # move forward for space
    t.pendown()                  # move turtle to surface
    t.fd(15)                     # move forward for dash line
    t.penup()                     # move turtle in air
    t.fd(20)                     # move forward for space

    #write clock integer
    t.write(str(val),align='center',font=('Arial',12,'normal'))

#coloured center
t.goto(2,-112)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.circle(5)
t.end_fill()

#hour hand
t.penup()
t.home()
t.rt(90)
t.pendown()
t.forward(100)
t.goto(-20,-64)
t.penup()

#write
t.goto(-30,-170)
t.pendown()
t.write('GfG Clock' ,font=('Arial',14,'normal'))

t.ht()
t.done()
