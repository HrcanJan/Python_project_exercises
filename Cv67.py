def maxx():
    i=int(input())
    j=i
    x=1
    max=1
    while(i!=0):
        i=int(input())
        if(i==j):
            x=x+1
        if(x>max):
            max=x
        if(i!=j):
            x=1
        j=i
    return max
            
        
x=maxx()
print(x)
    
