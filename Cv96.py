def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
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
