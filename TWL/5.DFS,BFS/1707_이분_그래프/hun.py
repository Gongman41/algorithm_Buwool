import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline


def check_bin(start):

    visited[start] = 1
    dq = deque([start])
    while dq:
        c = dq.popleft()
        for n in graph[c]:
            if visited[n] != 0:
                if visited[n] == visited[c]:
                    return False
            else:
                visited[n] = -visited[c]
                dq.append(n)
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    # print(graph)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    maru = 0
    visited = [0] * (V + 1)
    for start in range(1, V + 1):
        if visited[start] == 0:
            if check_bin(start) is False:
                print('NO')
                maru = -1
                break
            else:
                maru = 1

    if maru == 1:
        print('YES')

