import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


def dfs(i, now):
    global result
    que = deque([i])
    visited[i] = now
    while que:
        v = que.pop()
        now = visited[v]
        for to in edge[v]:
            if not visited[to]:
                que.append(to)
                visited[to] = now*(-1)
            else:
                if visited[to] == now:
                    result = 0
                    return


for tc in range(int(input())):
    V, E = map(int, input().split())

    edge = {i: [] for i in range(1, V+1)}

    for _ in range(E):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    visited = [0] * (V+1)

    result = 1

    for i in range(1, V+1):
        if not visited[i]:
            dfs(i, 1)
    # print(edge)
    # print(visited)
    if result:
        result = 'YES'
    else:
        result = 'NO'
    print(result)