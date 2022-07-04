def sqtt(n):
    s=n
    while ((s-(n/s))>0.00001):
        s=(s+(n/s))/2
    return s
def cos(a,b):
    return ((a/b)*60)

import turtle
n=100
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(135)
x=(n*n)+(n*n)
n=sqtt(x)
print(n)
turtle.forward(n)
turtle.left(180)
turtle.forward(n)
turtle.left(90)
turtle.forward(100)
x=(100*100)+(n*n)
n=sqtt(x)
print(n)
y=cos(100,n)
turtle.left(90+y)
print(y)
turtle.forward(n)
turtle.left(180)
turtle.forward(n)
turtle.left(90)
turtle.forward(100)
x=(100*100)+(n*n)
n=sqtt(x)
print(n)
y=cos(100,n)
turtle.left(90+y)
print(y)
turtle.forward(n)
turtle.left(180)
turtle.forward(n)
turtle.left(90)
turtle.forward(100)
x=(100*100)+(n*n)
n=sqtt(x)
print(n)
y=cos(100,n)
turtle.left(90+y)
print(y)
turtle.forward(n)
turtle.left(180)
turtle.forward(n)
turtle.left(90)
turtle.forward(100)
x=(100*100)+(n*n)
n=sqtt(x)
print(n)
y=cos(100,n)
turtle.left(90+y)
print(y)
turtle.forward(n)
turtle.left(180)
turtle.forward(n)
turtle.left(90)
turtle.forward(100)






