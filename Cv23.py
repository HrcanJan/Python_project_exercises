def nula(a, n, m):
    s=0
    for i in range(1):
        for j in range(m):
            if(a[i][j]==0):
                for i in range(n):
                    if(a[i][j]!=0):
                        break
                s=s+1
    return s
                                   

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
s=nula(a, n, m)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print(' ')
print(s)
                    
