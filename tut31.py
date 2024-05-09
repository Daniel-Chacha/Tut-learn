#a smiling emoji
import turtle as t 

t.bgcolor('black')
t.speed(40)

def mycircle(radius,color,x,y):
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(radius)
    t.end_fill()

#head
mycircle(100,'yellow',50,50)

# right eyes
mycircle(20,'white',10,170)
mycircle(7,'black',10,185)

#left eye
mycircle(20,'white',90,170)
mycircle(7,'black',90,185)

#nose
mycircle(15,'black',50,130)

def mysemicircle(rad,color,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.pensize(10)
    t.pencolor(color)
    
    t.setheading(90)
    t.circle(rad,extent=-180)

#tongue
mysemicircle(10,'red',60,92)

#mouth
mysemicircle(34,'black',85,125)




t.ht()
t.done()