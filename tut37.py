#create a digital clock
import turtle as t 
import datetime as dt 
import time

t.bgcolor('green')
t.pensize(4)


#obtain current time from the system
sec=dt.datetime.now().second
min=dt.datetime.now().minute
hr=dt.datetime.now().hour

t.penup()
t.goto(-20,0)
t.pendown()

#create rectangular box
for i in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(70)
    t.lt(90)

while True:
    t.ht()
    t.clear()
    #show time
    t.write(str(hr).zfill(2)
         + ':' + str(min).zfill(2) 
         + ':' + str(sec).zfill(2) ,font=('arial narrow',35,'bold'))
    time.sleep(1)
    sec+=1

    if sec==60:
        sec=0
        min+=1

    if min ==60:
        min=0
        hr+=1

    if hr==13:
        hr=1
        
