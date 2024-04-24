import sys
sys.stdin = open("input.txt")

'''
N명의 학생들의 줄을 세운다.
두학생의 키를 비교함
일부 학생만 비교함
'''
from collections import deque
N, M = map(int,input().split()) # N은 학생수 , M은 키를 비교한 횟수
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split()) # A학생은 B학생 앞에 서야한다.
    graph[A].append(B)
    indegree[B] += 1
## A 학생은 무조건 B학생의 앞에 서야하니까
result = []
queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    now = queue.popleft()
    result.append(now)

    for j in graph[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)

print(*result)

