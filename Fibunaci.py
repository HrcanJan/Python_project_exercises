def Fibunaci(n):
    if(n==1):
        return 1
    if(n==2):
        return 1
    n=Fibunaci(n-1)+Fibunaci(n-2)
    return n

print(Fibunaci(10))
