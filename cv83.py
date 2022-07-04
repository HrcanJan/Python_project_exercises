def any_lowercase1(s):
    for c in s:
        if not c.islower():
            return False
    return True

c='threedaysgrace'
s=any_lowercase1(c)
print(s)
