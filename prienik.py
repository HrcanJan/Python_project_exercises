def prienik(a, b, c, d):
    if(c<=a and d>=a and d<=b):
        return [a, d]
    if(c<=a and d>=a and d>=b):
        return [a, b]
    if(c>=a and d>=a and d<=b):
        return [c, d]
    if(c>=a and d>=a and d>=b):
        return [c, b]
    return [0,0]
            

def f(t):
    p=t[0]
    for item in t:
        p=prienik(p[0], p[1], item[0], item[1])
    if p[1]>p[0]:
        print()
        return True
    return False

t=[[0, 100],[-100, 5],[-75,50]]
a=f(t)
print(a)
