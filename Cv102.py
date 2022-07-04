def cumsum(t):
    s = 0
    x = []
    for i in t:
        s += i
        x.append(s)
    return x

t = [4, 5, 6]
s=cumsum(t)
print(s)
