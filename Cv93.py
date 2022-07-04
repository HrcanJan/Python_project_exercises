def avoids(a, b):
    for i in a:
        for j in b:
            if(i==j):
                return False
    return True
       
fin = open('words.txt')
n=1
k=1
b='aeiouy'
for line in fin:
    word = line.strip()
    x=avoids(word, b)
    if(x==True):
        print(word)
        k+=1
    n+=1
print((k/n)*100)
