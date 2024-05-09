#spiral web
import  turtle as t 

t.speed(40)
t.bgcolor('black')
colours=['red','yellow','orange','purple','green','blue']

for x in range(200):
    t.pencolor(colours[x%6])
    t.pensize(x/100 +1)
    t.forward(x)
    t.lt(59)

t.done()


