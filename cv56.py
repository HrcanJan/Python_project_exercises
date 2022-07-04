def bla(n):
    if(n==1):
        return 0
    s=bla(n-1)
    k=0
    for i in range(2,n):
        print(i, n)
        if(n%i==0):
            k=1
    if(k==0):
        s=s+n
    return s

x=int(input())
y=bla(x)
print(y)
