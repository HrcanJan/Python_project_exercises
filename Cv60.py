def maxx(n):
    x=int(input())
    max=x
    max2=x
    max3=x
    for i in range(n-1):
        x=int(input())
        if(x>max):
            max3=max2
            max2=max
            max=x
        if((x>max2 and x<max)or(max2==max)):
            max3=max2
            max2=x
        if((x>max3 and x<max2 and x<max)or(max3==max2)or(max3==max)):
            max3=x
    return max3
    
n=int(input())
if(n>=3):
    z=maxx(n)
    print(z)
