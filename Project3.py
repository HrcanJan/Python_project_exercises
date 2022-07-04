def polygon (t,l, n):
    for i in range(0,n,20):
        t.fd(l/n)
        t.lt(360/n)
def circle(t, r):
    l=2*r*3.141592
    n=100
    for i in range (20):
        polygon(bob,l,n)
        t.lt(180-360/20)
        polygon(bob,l,n)
        t.lt(180)

import turtle
bob = turtle.Turtle()
r=700
circle(bob,r)
