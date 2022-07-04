def prienik(a, b, c, m):
    c = [[0 for i in range(n)] for j in range(m)] 
    for i in range (n):
        for j in range (m):
            c[i][j]=a[i][j]*b[i][j]
    return c
            

n=int(input())
m=int(input())
a = [[0 for i in range(n)] for j in range(m)]
b = [[0 for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print(' ')
for i in range(n):
    for j in range(m):
        x=int(input())
        a[i][j]=x
for i in range(n):
    for j in range(m):
        x=int(input())
        b[i][j]=x
s=addition(a, b, n, m)
for i in range(n):
    for j in range(m):
        print(s[i][j], end=' ')
    print()
