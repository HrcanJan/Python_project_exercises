def maxx():
    i=int(input())
    max=i
    x=0
    while(i!=0):
        i=int(input())
        if(i>max):
            x=0
            max=i
        if(i==max):
            x=x+1
    return x
            
        
x=maxx()
print(x)
    
