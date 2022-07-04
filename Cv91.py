fin = open('words.txt')
for line in fin:
    word = line.strip()
    n=0
    if(len(word)>17):
        print(word)
