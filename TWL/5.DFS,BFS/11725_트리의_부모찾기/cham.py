import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    while q:    # q가 있을 때까지 반복
        now = q.popleft()
        for i in graph[now]:
            if parent[i] == 0:  # 부모 노드가 저장 되지 않은 상태라면
                parent[i] = now  # 현재 노드를 부모 노드로 저장
                q.append(i)


N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)    # 부모 노드 저장할 배열
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 무방향이니께
q = deque([1])  # 걍 처음부터 1 넣어줌

bfs()

for i in range(2, N+1):     # 2번 노드부터 출력
    print(parent[i])