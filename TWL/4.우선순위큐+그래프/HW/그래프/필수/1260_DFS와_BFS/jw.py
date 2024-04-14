import sys
input = sys.stdin.readline
from collections import deque
import copy

N, M, V = map(int, input().split())

link = {}
for i in range(1, N+1):
    link[i] = []
    
for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for i in link.keys():
    link[i] = deque(sorted(link[i]))

link2 = copy.deepcopy(link)

def dfs(V, visited=[]):
    visited.append(V)
    for v in link[V]:
        if v not in visited:
            visited = dfs(v, visited)

    return visited
    
def bfs(l, V):
    visited = []
    que = deque()
    que.append(V)
    
    while que:
        v = que.popleft()

        if v not in visited:
            visited.append(v)
            temp = l.pop(v)
            
            while temp:
                if temp[0] in visited:
                    temp.popleft()
                    continue
                else:
                    que.append(temp.popleft())

    print(*visited)

DFS = dfs(V)
print(*DFS)

bfs(link2, V)
