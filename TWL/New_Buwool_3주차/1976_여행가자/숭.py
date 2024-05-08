import sys
from collections import deque

def bfs(start):
    dq = deque([start])
    visited[start] = 1

    while dq:
        now = dq.popleft()

        for i in range(n):
            if cities[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dq.append(i)

n = int(input())
m = int(input())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
plan = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))

visited = [0 for _ in range(n)]
# 첫번째 방문할 도시를 기준으로 어떻게든 갈 수 있으면 갈 수 있는 거임
bfs(plan[0])

for city in plan:
    if visited[city] == 0:
        print("NO")
        break
else:
    print("YES")