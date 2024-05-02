import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
nodes = [[] for _ in range(n+1)]
visited = [0]*(n+1)
max_n = 0
start = 0
for _ in range(n-1):
    par,chd,leng = map(int,input().split())
    nodes[par].append([chd,leng])
    nodes[chd].append([par,leng])
deq = deque([[1,0]])
visited[1] = 1
while deq:
    node,total_len = deq.popleft()
    if max_n <= total_len:
        max_n = total_len
        start = node
    if nodes[node]:
        for next,next_len in nodes[node]:
            if visited[next] == 0:
                visited[next] = 1
                deq.append([next,total_len+next_len])
deq.append([start,0])
visited = [0]*(n+1)
visited[start] = 1
while deq:
    node,total_len = deq.popleft()
    if max_n <= total_len:
        max_n = total_len
    if nodes[node]:
        for next,next_len in nodes[node]:
            if visited[next] == 0:
                visited[next] = 1
                deq.append([next,total_len+next_len])
print(max_n)
    

    
    