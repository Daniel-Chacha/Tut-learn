#draw a panda
import turtle as t 
t.bgcolor('green')

#define a method to draw circles
def ring(colour,rad):
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

#draw first ear
t.penup()
t.setpos(-35,95)
t.pendown()
ring('black',15)

#draw second ear
t.penup()
t.setpos(35,95)
t.pendown()
ring('black',15)

#face
t.penup()
t.setpos(0,35)
t.pendown()
ring('white',40)
    
#draw the eyes black
t.penup()
t.setpos(-18,75)
t.pendown()
ring('black',8)

t.penup()
t.setpos(18,75)
t.pendown()
ring('black',8)

#draw eyes white
t.penup()
t.setpos(-18,77)
t.pendown()
ring('white',4)

t.penup()
t.setpos(18,77)
t.pendown()
ring('white',4)

#draw nose
t.penup()
t.setpos(0,55)
t.pendown()
ring('black',5)

#draw mouth
t.penup()
t.setpos(0,55)
t.pendown()
t.rt(90)
t.circle(5,180)
t.penup()
t.setpos(0,55)
t.pendown()
t.lt(360)
t.circle(5,-180)

t.ht()

t.done()