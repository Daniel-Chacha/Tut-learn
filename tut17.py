#alternatively
import turtle as t 

def semi_circle(colour,rad,position):
    t.pencolor(colour)
    t.circle(rad,-180)
    t.penup()
    t.setpos(position,0)
    t.pendown()
    t.right(180)

colour=['violet', 'indigo', 'blue', 
       'green', 'yellow', 'orange', 'red']
t.bgcolor('black')
t.pensize(10)
t.right(90)
t.speed(70)

for x in range(7):
    semi_circle(colour[x], 10*(x+5), -10*(x+1))

t.ht()
t.done()