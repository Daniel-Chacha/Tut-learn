#a bar chart
import turtle as t 

t.speed(0)

t.penup()
t.setpos(-280,-250)
t.setheading(0)
t.pendown()

def bar(length,colour):
    
         t.fillcolor(colour)
         t.begin_fill()
         t.fd(50)
         t.lt(90)
         t.fd(length)
         t.lt(90)
         t.fd(50)
         t.lt(90)
         t.fd(length)
         t.setheading(0)
         t.fd(50)
 
         t.end_fill()

l=['300','150','200','50','10','210','40','400']
c=['red','orange','purple','green','blue','violet','black','maroon']
for i in range(8):
       bar(float(l[i]),c[i])

       
t.ht()
t.done()
