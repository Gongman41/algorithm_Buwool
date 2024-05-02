import sys
sys.setrecursionlimit(10**6)


def bt(now, sum_, cnt, start):
    global result

    if sum_ >= result:
        return

    if cnt == N:
        result = sum_
        return

    if cnt == N-1:
        if arr[now][start]:
            bt(start, sum_ + arr[now][start], cnt+1, start)
        return

    for to in range(N):
        if to == now or to == start:
            continue

        if arr[now][to] and not visited[to]:
            visited[to] = 1
            bt(to, sum_ + arr[now][to], cnt+1, start)
            visited[to] = 0


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

result = int(1e9)
for i in range(N):
    visited = [0] * N
    bt(i, 0, 0, i)
print(result)

