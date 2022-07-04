def even(n):
    x=int(input())
    if(n==1):
        if(x%2==0):
            return 'true'
        return 'false'
    s=even(n-1)
    if(x%2==1):
        if(s=='true'):
            return 'false'
        return 'true'
    else:
        return s

x=int(input())
y=even(x)
print(y)
