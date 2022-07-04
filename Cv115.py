def reverse_pair(word1, word2):
    a=sorted(word2)
    if(a==word1):
        return True
    else:
        return False


f = open('words.txt')
for line in f:
    word = line.strip()
    word2 = line.strip()
    x=reverse_pair(word, word2)
    if(x==True):
        print(word)
