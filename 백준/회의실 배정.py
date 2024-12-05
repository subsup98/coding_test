import sys
n = int(sys.stdin.readline())
answer= 1
time_table=[]
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append((start,end))
time_table.sort(key=lambda x: (x[1],x[0]))
end = time_table[0][1]
for i in range(1,n):
    if time_table[i][0]>=end:
        end =time_table[i][1]
        answer +=1
print(answer)