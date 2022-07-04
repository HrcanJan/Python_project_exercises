def maxx():
    i=int(input())
    max=i
    y=1
    x=1
    while(i!=0):
        i=int(input())
        y=y+1
        if(i>max):
            max=i
            x=y
    return x     
        
x=maxx()
print(x)
    
