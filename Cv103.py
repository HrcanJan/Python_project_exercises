def middle(t):
    x = []
    for i in range(1,len(t)-1):
        x.append(t[i])
    return x

t = [4, 5, 6, 7, 8, 9]
s=middle(t)
print(s)
