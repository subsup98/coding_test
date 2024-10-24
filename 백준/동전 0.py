import sys
n, k = map(int,sys.stdin.readline().split())
answer=0
coins=[]

for i in range(n):
    c=int(sys.stdin.readline().rstrip())
    coins.append(c)
coins.reverse()
for coin in coins:
    if k>=coin:
        answer += k//coin
        k %= coin
        if k<=0:
            break
print(answer)
    