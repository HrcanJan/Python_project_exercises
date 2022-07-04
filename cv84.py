def f(x, n):
    b=''
    for i in x:
        if(ord(i)+n>97+26):
            b=b+chr(ord(i)+n-26)
        if(ord(i)+n<97):
            b=b+chr(ord(i)+n+26)
        else:
            b=b+chr(ord(i)+n)
    return b

a='melon'
n=-10
b=f(a, n)
print(b)
        
