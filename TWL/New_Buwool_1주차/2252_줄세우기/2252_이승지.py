# 순서가 정해져 있고 비교한 결과가 간선이라고 생각
# 몇 개에 키에 대한 비교 결과가 없는 경우 여러 답이 가능하다고 생각하면 됨, 그 중 하나 출력하랬으이까 이건 무시

from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

dq = deque()
for i in range(1, n+1):
    if in_degree == 0:
        # 여긴 넣는 순서 상관 없음
        dq.append(i)

answer = []
while dq:
    now = dq.popleft()
    answer.append(now)
    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            dq.append(i)

print(*answer)