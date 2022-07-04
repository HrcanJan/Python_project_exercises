def nula(a, n, m):
    max=a[0][0]
    for i in range(n):
        for j in range(m):
            if(a[i][j]>max):
                max=a[i][j]
    return max
                                   

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
print(s)
                    
