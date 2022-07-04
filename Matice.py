def f(a, b):
    if(len(a[0])!=len(b) or len(b[0])!=len(a)):
        return -1
    c=[]
    n=(len(a))
    m=len(a[0])
    for i in range(n):
        c.append([])
        for j in range(n):
            x=0
            for i1 in range(m):
                x+=a[i][i1]*b[i1][j]
            c[i].append(x)
    return c

n=2
m=3
o=3
p=2
a=[]
b=[]
for i in range(n):
    a.append([])
    for j in range(m):
        x=int(input())
        a[i].append(x)
for i in range(o):
    b.append([])
    for j in range(p):
        x=int(input())
        b[i].append(x)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print(' ')
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print(' ')
c=f(a, b)
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j], end=' ')
    print(' ')
