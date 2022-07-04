def is_anagram(t1, t2):
    return sorted(t1) == sorted(t2)

t1 = 'abcdefg'
t2 = 'fagdecb'
s=is_anagram(t1, t2)
print(s)
