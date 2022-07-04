def addition(a, b, n, m):
    s=[]
    for i in range (n):
        s.append([])
        for j in range (m):
            x=a[i][j]+b[i][j]
            s[i].append(x)
    return s
            

n=int(input())
m=int(input())
a = [[0 for i in range(n)] for j in range(m)]
b = [[0 for i in range(n)] for j in range(m)] 
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
    print(' ')
