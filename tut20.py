#a diamond
import turtle as t

t.speed(100)
t.penup()
t.setpos(50,50)
t.pendown()
#big triangle
t.fd(248)
t.rt(120)
t.fd(250)
t.rt(120)
t.fd(250)

#small triangles inside the big triangle
t.rt(120)
t.fd(62)
t.rt(73.5)
t.fd(225)
t.lt(163.5)
t.fd(217)
t.rt(90)
t.fd(62)
t.rt(106)
t.fd(229)

t.backward(229)


t.lt(105)
t.fd(63)
#small triangles on top
t.lt(120)
t.fd(70)
t.lt(125)
t.fd(70)
t.rt(120)
t.fd(67)
t.lt(125)
t.fd(62)
t.rt(125)
t.fd(67)
t.lt(120)
t.fd(62)
t.rt(125)
t.fd(65)
t.lt(120)
t.fd(63)

#line on top of 4 triangles
t.backward(63)
t.lt(121)
t.fd(200)


t.ht()
t.done()

