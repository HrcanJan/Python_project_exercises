def polygon (t,l, n):
    for i in range(0,n,2):
        t.fd(l/n)
        t.lt(120/n)
def circle(t, r):
    l=2*r*3.141592
    n=100
    t.lt(30)
    for i in range (2):
        for i in range (6):
            polygon(bob,l,n)
            t.lt(120)
            polygon(bob,l,n)
            t.lt(180)
        t.lt(30)

import turtle
bob = turtle.Turtle()
r=100
circle(bob,r)
