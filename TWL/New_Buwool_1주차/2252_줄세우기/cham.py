import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def topological():
    global result
    while q:
        now = q.popleft()
        result.append(now)
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)      # 진입차수
result = []
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a -> b 의미함
    indegree[b] += 1    # b의 진입 차수 + 1

for i in range(1, N+1):
    if indegree[i] == 0:    # 진입 차수 0인 것만 q에 넣어준다
        q.append(i)

topological()
print(*result)
