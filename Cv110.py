def chop(t):
    del t[0]
    del t[len(t)-1]

t=[1, 2, 3, 4, 5, 6, 7, 8]
chop(t)
print(t)
