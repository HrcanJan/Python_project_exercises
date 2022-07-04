def f(t):
    s=0
    i=0
    for i in range(len(t)):
        k=0
        j=0
        for j in range(i):
            if(t[i]==t[j]):
                k=1
        if(k==0):
            s+=1
    return s

t = [2, 6, 8, 6, 2, 9, 8]
s=f(t)
print(s)
