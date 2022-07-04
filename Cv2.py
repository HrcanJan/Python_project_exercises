def f(a):
    x='a'
    c=[]
    for i in range(len(a)):
        for j in a[i]:
            if(j=='a'):
                c.append(a[i])
                break
    return c

a=['aoj', 'dod', 'mama', 'print', 'aaa']
b=f(a)
print(b)
    
