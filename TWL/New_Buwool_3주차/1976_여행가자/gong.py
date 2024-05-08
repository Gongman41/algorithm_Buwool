from collections import deque

def bfs(start,next):
    visited = [0]*(N+1)
    deq = deque([start])
    visited[start] = 1
    while deq:
        cur = deq.popleft()
        if cur == next:
            return True
        for i in range(1,N+1):
            if graph[cur][i] and not visited[i]:
                visited[i] = 1
                deq.append(i)
    return False
N = int(input())
M = int(input())
graph = [0]
for _ in range(N):
    graph.append([0]+list(map(int,input().split())))
    
plan = list(map(int,input().split()))

for i in range(M-1):
    check = bfs(plan[i],plan[i+1])
    if check == False:
        print('NO')
        break
else:
    print('YES')