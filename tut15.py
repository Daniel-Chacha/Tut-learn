#a heart
import turtle as t 
t.speed(100)
t.pensize(5)

#a curve
def curve():
    for x in range(200):
        t.right(1)
        t.fd(1)

#draw a full heart
def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)

    curve()
    t.left(120)
    curve()
    t.fd(112)
    t.end_fill()

#text
def txt():
    t.penup()
    t.setpos(-68,95)
    t.pendown()

    t.write('geeks for geeks',font=('verdana',12,'bold'))

heart()
txt()

t.ht()
t.done()