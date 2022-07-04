def formulas(s, file):
    x = []
    for k in s:
        pom = ""
        for i in k:
            word = "m"
            for j in pom:
                word += "-" + j + "_c+" + j + "_p"
            word += ">=" + i + "_c"
            x.append(word)
            del word
            pom += i
        del pom
    pom = []
    for i in x:
        if i not in pom:
            pom.append(i)
    for i in pom:
        file.write(i)
        file.write("\n")
    file.write("\n")

def compare(s, s2, n):
    for i in range(len(s2)):
        if(s[i] != s2[i]):
            return False
    return True

def bad(s, j, file):
    word = "m"
    for i in s:
        word += "-" + i + "_c+" + i + "_p"
    word += "<" + j + "_c"
    file.write(word)
    file.write("\n")

def createnew(s, a, n, fin, file):
    row = []
    for i in s:
        for j in a:
            col = ""
            k = 0
            fin.seek(0)
            for line in fin:
                word = line.strip()
                if(n >= len(word)):
                    continue
                if(compare(word, i, n) and word[n] == j):
                    k = 1
                    col += i + j
                    break
            if(k == 0):
                bad(i, j, file)
            else:
                row.append(col)
    return row

def antiformulas(m, a, fin, file):
    s = []
    for i in a:
        k = 0
        fin.seek(0)
        for line in fin:
            word = line.strip()
            if(word[0] == i):
                k = 1
                s.append(i)
        if(k == 0):
            i += "_c"
            file.write("m<")
            file.write(i)
            file.write("\n")
    for k in range(1, m + 1):
        pom = []
        for i in s:
            if i not in pom:
                pom.append(i)
        s = pom
        s = createnew(s, a, k, fin, file)
        del pom

import sys
fin = open(sys.argv[1], "r")
file = open(sys.argv[2], "w")
alphabet = ""
s = []
m = 0
for line in fin:
    word = line.strip()
    s.append(word)
    if(m < len(word)):
        m = len(word)
    for i in word:
        k = 0
        for j in alphabet:
            if(j == i):
                k = 1
        if(k == 0):
            alphabet += i
formulas(s, file)
antiformulas(m, alphabet, fin, file)
fin.close()
file.close()
