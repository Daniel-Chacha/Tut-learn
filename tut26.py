# a hut
import turtle as t 
import math

t.bgcolor('black')
t.speed(10)

#function for drawing rectangle
def drawrectangle(t,width,height,color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

#function to draw equilateral triangle
def drawtriangle(t,length,color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(length)
    t.left(135)
    t.fd(length/math.sqrt(2))
    t.left(90)
    t.fd(length/math.sqrt(2))
    t.left(135)
    t.end_fill()

#a function to draw  a parallelogram ;walls
def drawparallelogram(t,width,height,color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.fd(width)
    t.lt(60)
    t.fd(height)
    t.lt(120)
    t.fd(width)
    t.lt(60)
    t.fd(height)
    t.lt(90)
    t.end_fill()


#draw the front of the house
t.penup()
t.setpos(-150,-120)
t.pendown()
drawrectangle(t,100,110,'blue')

#draw the front door
t.penup()
t.goto(-120,-120)
t.pendown()
drawrectangle(t,40,60,'lightgreen')

#front roof
t.penup()
t.goto(-150,-10)
t.pendown()
drawtriangle(t,100,'magenta')

#sidewall of the house
t.penup()
t.goto(-50,-120)
t.pendown()
drawparallelogram(t,60,110,'yellow')

#window
t.penup()
t.goto(-30,-60)
t.pendown()
drawparallelogram(t,20,30,'brown')

#draw sideroof
t.penup()
t.goto(-50, -10)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.left(30)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(75)
t.forward(60)
t.left(105)
t.forward(100 / math.sqrt(2))
t.left(45)
t.end_fill()


t.done()



#positions=[['-200','-187.5'],['-200','-125'],['-200','-62.5'],['-200','0'],['-200','62.5'],['-200','125',],['-200','187.5']]