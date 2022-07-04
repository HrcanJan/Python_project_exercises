def uses_all(b, a):
    for i in a:
        k=False
        for j in b:
            if(k==True):
                continue
            if(i==j):
                k=True
        if(k==False):
            return False
    return True
       
fin = open('words.txt')
n=1
k=1
b='acefhlo'
for line in fin:
    word = line.strip()
    x=uses_all(word, b)
    if(x==True):
        print(word)
        k+=1
    n+=1
print((k/n)*100)
