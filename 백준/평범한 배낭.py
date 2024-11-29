import sys
n,k = map(int, sys.stdin.readline().split())
items=[]
table=[[0]*(k+1)for i in range(n+1)]
for i in range(n):
    w,v=map(int, sys.stdin.readline().split())
    items.append((w,v))
for i in range(1,n+1):
    for j in range(1, k+1):
        if j >=items[i-1][0]:
            table[i][j]=max(items[i-1][1]+table[i-1][j-items[i-1][0]],table[i-1][j])
        else:
            table[i][j]=table[i-1][j]
print(table[n][k])
