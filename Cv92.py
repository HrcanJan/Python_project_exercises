def noe(a):
    for i in a:
        if(i=='e'):
            return False
    return True
       
fin = open('words.txt')
n=1
k=1
for line in fin:
    word = line.strip()
    x=noe(word)
    if(x==True):
        k+=1
    n+=1
print((k/n)*100)
