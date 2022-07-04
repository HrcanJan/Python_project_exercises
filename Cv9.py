def is_abecedarian(a):
    k=False
    j=1
    for i in a:
        j=i+1
        for j in a:
            if(ord(i)<=ord(j)):
                k=True
            else:
                return False
    return True
       
fin = open('words.txt')
n=1
k=1
for line in fin:
    word = line.strip()
    x=is_abecedarian(word)
    if(x==True):
        print(word)
        k+=1
    n+=1
print((k/n)*100)
