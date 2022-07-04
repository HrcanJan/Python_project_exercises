def even(n):
    if(n==0):
        return 0
    x=int(input())
    s=even(n-1)
    if(x%2==0):
        s=s+1
    return s

x=int(input())
y=even(x)
print(y)
