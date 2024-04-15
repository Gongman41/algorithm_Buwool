import sys
sys.stdin = open('input.txt')
from collections import deque

def dfs(n):
    print(n, end=' ')
    visited_1[n] = 1
    for node in graph[n]:
        if not visited_1[node]:
            visited_1[node] = 1
            dfs(node)

def bfs(n):
    queue = deque([n])
    visited_2[n] = 1
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for node in graph[now]:
            if not visited_2[node]:
                queue.append(node)
                visited_2[node] = 1

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은!!! 것을 먼저 방문

N, M, V = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향이니까 !
    graph[x].sort()
    graph[y].sort()

visited_1 = [0] * (N+1)
visited_2 = [0] * (N+1)

dfs(V)
print()
bfs(V)