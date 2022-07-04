def add(n):
    if(n==0):
        return 1
    x=int(input())
    s=add(n-1)
    s=s*x
    return s

x=int(input())
y=add(x)
print(y)
