def f(t):
    s = 0
    i = 0
    while(i<len(t)):
        if(t[i]>t[i-1]):
            if(t[i]>t[i+1]):
                s+=1
        i+=1
    return s

t = [5, 4, 9, 8, 2, 3, 1, 0]
s=f(t)
print(s)
