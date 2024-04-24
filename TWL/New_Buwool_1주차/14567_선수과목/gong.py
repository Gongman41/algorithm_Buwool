from collections import deque
import sys
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited= [0]*(N+1)
result = [0]*(N+1)
for _ in range(M):
    sun,hu = map(int,sys.stdin.readline().split())
    graph[sun].append(hu)
    visited[hu] += 1
deq = deque([])
for i in range(1,N+1):
    if visited[i] == 0:
        deq.append([i,1])
while deq:
    cur,count = deq.popleft()
    result[cur] = count
    for next in graph[cur]:
        visited[next] -= 1
        if visited[next] == 0:
            deq.append([next,count+1])
    
for i in range(1,N+1):
    print(result[i],end=' ')
        

