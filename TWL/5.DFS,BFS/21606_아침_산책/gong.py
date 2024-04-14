# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
# # 기본 트리, 시작점과 끝 점은 실내. 이외에는 실외.
# N = int(input())
# A = input()
# Node = [0]
# visited = [0]*(N+1)
# for i in range(N):
#     Node.append(int(A[i]))
# tree = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     parent,child = map(int,sys.stdin.readline().split())
#     tree[child].append(parent)
#     tree[parent].append(child)
# # 모든 정점에서 탐색. 시작점에 실내인 경우에 탐색. 실내일때 끝
# # 

# deq = deque([])
# cnt = 0
# for i in range(1,N+1):
#     if Node[i] == 1:
#         deq.append([i,0])
#         while deq:
#             cur,last = deq.popleft()
            
#             for t in tree[cur]:
#                 if t == last:
#                     continue
#                 if Node[t] == 0:
#                     deq.append([t,cur])
#                 else:
                    
#                     cnt+=1
# # 힌반 간 곳 2번으로 체크해서 중복으로 안하도록
# # 시간 줄일려면 실외부터 탐색하는게 맞다/
            
# print(cnt)
        
        
    

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

A = input().rstrip()

graph = [[] for _ in range(n+1)]
place = [0] * (n+1)
visited = [0] * (n+1)

for i in range(len(A)):
    if A[i] == '1':
        place[i+1] = 1

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node):
    res = 0 
    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                res += dfs(next_node)
        else:
            res += 1
    return res

ans = 0
for i in range(1, n+1):
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res - 1)
    else:
        for next_node in graph[i]:
            if place[next_node] == 1:
                ans += 1
print(ans)
    
