def addition(a, n ,m):
    max=0
    q=0
    for i in range(1):
        for j in range(m):
            s=0
            for i in range(n):
                s=s+a[i][j]
            if(s>max):
                max=s
                q=j
    return q
                                   

n=int(input())
m=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        x=int(input())
        a[i].append(x)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print(' ')
q=addition(a, n, m)
print(q+1)
