# import sys

# # 재귀 호출의 깊이 한계를 늘림
# sys.setrecursionlimit(10 ** 8)

# def Recur(a):
#     if not Nodes[a][0] and visited[a] == 0:
#         result.append(a)
#         visited[a] = 1
#     elif Nodes[a][0] and visited[a] == 0:
#         for i in Nodes[a][0]:
#             if visited[i] == 0:
                
#                 Recur(i)
#         visited[a] = 1
#         result.append(a)
        
# N,M = map(int,input().split())
# Nodes = [[[],[]] for _ in range(N+1)]
# for _ in range(M):
#     par,chl = map(int,input().split())
#     Nodes[par][1].append(chl)
#     Nodes[chl][0].append(par)
# visited = [0]*(N+1)
# result = []

# for i in range(1,N+1):
#     Recur(i)
        
# print(*result)
# 유니온 파인드 느낌

import sys
from collections import deque
N,M = map(int,input().split())
Nodes = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    par,chl = map(int,sys.stdin.readline().split())
    Nodes[par].append(chl)
    visited[chl] += 1
result = []
queue = deque([])
for i in range(1,N+1):
    if visited[i] == 0:
        queue.append(i)
while queue:
    current = queue.popleft()
    result.append(current)
    for i in Nodes[current]:
        visited[i] -= 1
        if visited[i] == 0:
            queue.append(i)
for j in result:
    print(j,end=' ')


    
        
    