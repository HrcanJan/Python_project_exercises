def mysqrt(n):
    print('a mysqrt(a) math.sqrt(a) diff')
    print('- --------- ------------ ----')
    i=1
    while(i<=n):
        s=i
        while((s-(i/s))>0.00001):
            s=(s+(i/s))/2
        print(s)
        q=math.sqrt(i)
        print(q)
        i=i+1
        
import math   
n=int(input())       
x=mysqrt(n)
print(x)
    
