def psum(t):
    s = 0
    for i in t:
        s += sum(i)
    return s

t = [[1, 2], [3], [4, 5, 6]]
s=psum(t)
print(s)
