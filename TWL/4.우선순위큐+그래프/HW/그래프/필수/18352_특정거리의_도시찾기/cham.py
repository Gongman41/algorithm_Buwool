import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        now = q.popleft()
        for city in graph[now]:
            if distance[city] == -1:
                distance[city] = distance[now] + 1
                q.append(city)


# N: 도시 개수, M: 도로 개수, K: 거리 정보, X: 출발 도시의 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)   # X와 다른 도시 간 거리 넣어줄 배열
distance[X] = 0     # 출발지는 0으로! 거리를 인접 도시에 1 더해서 물려주는 느낌
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

q = deque([X])
bfs()
# print(distance)
if K in distance:   # 최단거리가 K인 도시가 있는 경우
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
else:       # 최단거리가 K인 도시가 없는 경우
    print(-1)