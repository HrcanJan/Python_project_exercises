def maxx():
    i=int(input())
    j=i
    x=0
    while(i!=0):
        i=int(input())
        if(i>j):
            x=x+1
        j=i
    return x
            
        
x=maxx()
print(x)
    
