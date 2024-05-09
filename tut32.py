#tangent circles
import turtle as t 
r=10
n=10

for x in range(1,n+1,1):
    t.circle(r*x)



#alternatively
r=10
for x in range(10):
    t.circle(r)
    r+=10

t.done()