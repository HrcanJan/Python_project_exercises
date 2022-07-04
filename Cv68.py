def fibonacci(x):
    n=0
    i=0
    j=1
    k=0
    while(x>n):
        n=i+j
        i=j
        j=n
        k=k+1
    if(x==n):
        return k
    else:
        return -1
        
            
n=int(input())       
x=fibonacci(n)
print(x)
    
