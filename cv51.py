def add(n, s):
    if(n==0):
        return 0
    s=add(n-1, s)
    s=s+n
    return s

x=int(input())
s=0
y=add(x, s)
print(y)
