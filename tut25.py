#colourful star pattern
import turtle as t 
import random

t.speed('fastest')

def draw(n,x,angle):
    for i in range(n): #loop for number of stars
        t.colormode(255)

         #generate random number btwn 0 and 255
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)

         #setting outline and fill colour
        t.pencolor(a,b,c)
        t.fillcolor(a,b,c)

        t.begin_fill()

        for j in range(5):    #loop for drawing each star
            t.fd(5 * n-5 * i)
            t.rt(x)
            t.fd(5 * n-5 * i)
            t.rt(72 -x)
        
        t.end_fill()

        #rotation for the next star
        t.rt(angle)

#setting the parameters
n=30   #no. of stars
x=144    #exterior angle of each star
angle=18   #  angle of rotation for the spiral

draw(n,x,angle)

t.done()
 