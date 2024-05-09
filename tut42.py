
# import package
import turtle 
 
# loop for printing some stamps
for i in range(15):
     
    # for motion
    turtle.forward(100+10*i)
     
    # printing turtle shape
    turtle.stamp()
     
    # for pattern
    turtle.right(90)

turtle.done()