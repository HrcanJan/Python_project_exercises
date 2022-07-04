def gcd(a, b):
    if(a==0):
       return b 
    if(b==0):
       return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


a=int(input())
b=int(input())
x=gcd(a, b)
print(x)
        
