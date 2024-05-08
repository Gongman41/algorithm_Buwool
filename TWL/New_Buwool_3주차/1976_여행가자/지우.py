import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
link = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

par = [i for i in range(N)]

start = plan[0] - 1
par[start] = -1
que = deque([start])

while que:
    now = que.popleft()
    for next_ in range(N):
        if link[now][next_] and par[next_] == next_:
            par[next_] = start
            que.append(next_)

par[start] = start
plan_set = set(plan)
for city in plan_set:
    city -= 1
    if par[city] != start:
        exit(print('NO'))
print('YES')

'''
    다른 경로 통해서도 갈 수만 있으면 됨
    시작점 부터 출발해서
    갈 수 있는 모든 경로에 1
'''
