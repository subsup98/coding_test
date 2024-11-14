import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())

max_time =100000
visited = [0]*(max_time+1)
def bfs():
    q =deque()
    q.append(n)

    while q:
        x=q.popleft()
        moves=[x-1,x+1,x*2]
        if x == k:
            print(visited[x])
            break
        for move in moves:
            if 0 <= move <= max_time and not visited[move]:
                visited[move]=visited[x]+1
                q.append(move)
bfs()