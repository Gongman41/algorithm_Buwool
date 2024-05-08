import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(start):
    dq.append(start)
    visited[start] = 1
    while dq:
        now = dq.popleft()
        for i in range(N):
            if graph[now][i] == 1 and visited[i] == 0:
                dq.append(i)
                visited[i] = 1

N = int(input())
M = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))  # 나중에 -1 해야 함
# print(graph)
visited = [0] * (N+1)
dq = deque()
dfs(plans[0] - 1)   # 출발지를 bfs 인자로

for city in plans:
    if visited[city-1] == 0:
        print('NO')
        break
else:
    print('YES')