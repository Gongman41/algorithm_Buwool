import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:    # 진입차수 0이면
            q.append(i)

    while q:
        now = q.popleft()
        visited[now] += 1
        for n_node in graph[now]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                # 이전 노드 값과 같이 해주고 나중에 popleft 해줄 때 + 1
                visited[n_node] = visited[now]
                q.append(n_node)

    for node in range(1, n+1):
        print(visited[node], end=' ')

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)      # 노드 진입차수 저장할 변수
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1    # a -> b 니까 b의 진입차수 + 1

topology_sort()

