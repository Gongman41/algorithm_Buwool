import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())
    line = deque(list(map(int, input().split())))
    link = {i:[] for i in range(V+1)}
    e_list = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = line.popleft(), line.popleft()
        link[s].append(e)
        e_list[e].append(s)

    que = deque([])
    for i in range(1, V+1):
        if e_list[i] == []:
            que.append(i)

    visited = [False] * (V+1)
    arr = []
    while que:
        v = que.popleft()
        visited[v] = True
        arr.append(v)
        
        for nxt in link[v]:
            if len(e_list[nxt]) >= 2:
                e_list[nxt].remove(v)
            elif not visited[nxt]:
                que.append(nxt)
    result = ' '.join(map(str, arr))
    print(f'#{tc} {result}')


