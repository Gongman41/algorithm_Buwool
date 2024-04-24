# import sys
# sys.stdin = open('input.txt')

# '''
# 선수과목을 이수해야, 이수할 수 있는 과목이 있음
# 선수과목을 반드시 키져야하는데, 각각 언제 전공과목을 이수할 수 있을까
# 한학기에 제한은 없고, 매학기 항상 개설된다.
# 최소 몇학기가 걸리는지 프로그램을 작성한다.
# '''

# from collections import deque

# N, M = map(int,input().split())
# graph = [[] for _ in range(N+1)]
# indegree = [0] * (N+1)
# result = [0] * (N+1)
# for i in range(M):
#     A, B = map(int,input().split())
#     graph[A].append(B)
#     indegree[B] += 1

# queue = deque()

# for i in range(1,N+1):
#     if indegree[i] == 0:
#         queue.append(i)
# while queue:
#     now = queue.popleft()
#     for j in graph[now]:
#         indegree[j] -= 1
#         if indegree[j] == 0:
#             queue.append(j)
#             result[j] += result[now] + 1

# for r in result[1:]:
#     print(r + 1, end= ' ')

from collections import deque
import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())
lst = list([] for _ in range(n+1))

for _ in range(m):
    a, b = map(int, input().split())
    lst[b].append(a)

result = [0] * (n+1)
dq = deque()

for num in range(1, n+1):
    if not lst[num]:
        dq.append(num)

while dq:
    check_1 = dq.popleft()
    for j in range(1, n+1):
        if check_1 in lst[j]:
            dq.append(j)
            result[j] += result[check_1] + 1
for kkk in range(1, n+1):
    print(result[kkk]+1,end = ' ')