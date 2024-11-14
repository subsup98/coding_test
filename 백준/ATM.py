import sys
n =int(sys.stdin.readline().strip())
time = list(map(int,sys.stdin.readline().strip().split()))
time.sort()
print(time)
ans=0
for i in range(len(time)-1):
    ans +=time[i]
    time[i+1]= time[i+1]+time[i]
print(ans+time[-1])
