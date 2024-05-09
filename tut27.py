#chess board
import turtle as t

t.setup(900,700)
t.speed(100)
t.pensize(5)

def draw(t,length,width):
    for x in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)

t.penup()
t.goto(-200,-250)
t.pendown()
draw(t,500,500)

positions1=[['-200','-187.5'],['-200','-125'],['-200','-62.5'],['-200','0'],['-200','62.5'],['-200','125',],['-200','187.5'],['-200','250']]
positions2=[['-137.5','250'],['-75','250'],['-12.5','250'],['50','250'],['112.5','250'],['175','250',],['237.5','250']]


def line(t,pos):
    for a in pos:
        
        x,y=map(float,a)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.fd(500)
        

line(t,positions1)

t.rt(90)
line(t,positions2)

t.ht()
t.done()