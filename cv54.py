def even(n):
    x=int(input())
    if(n==1):
        return x
    max=even(n-1)
    if(x>max):
        max=x
    return max

x=int(input())
y=even(x)
print(y)
