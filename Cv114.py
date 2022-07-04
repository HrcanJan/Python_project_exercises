def has_duplicates(a, n):
    for i in range(n):
        for j in range(n):
            for i1 in range(n):
                for j1 in range(n):
                    if(i==i1 and j==j1):
                        continue
                    if(a[i][j]==a[i1][j1]):
                        return True                  
    return False

n=int(input())
a=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=int(input())
x=has_duplicates(a, n)
print(x)
