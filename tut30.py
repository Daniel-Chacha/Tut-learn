#hexagons inside bigger hexagon
import turtle as t 

t.setup(900,700)
t.speed(50)
t.pensize(5)

def drawhexagon(side,angle):
    for x in range(6):
        t.fd(side)
        t.lt(angle)
        side-=5
        

side=150
angle=60

for i in range(5):
    drawhexagon(side,angle)
    side-=30

t.ht()
t.done()
