def is_sorted(t):
    c=t[0]
    for i in t:
        if(i<c):
            return False
        c=i
    return True

t = [4, 5, 2, 7, 8, 9]
s=is_sorted(t)
print(s)
