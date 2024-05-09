#get co ordinates on the screen
import turtle  as t 

t.speed(10)

def pos(x,y):
    print('{0},{0}'.format(x,y))

t.onscreenclick(pos,1)
t.listen()
t.done()