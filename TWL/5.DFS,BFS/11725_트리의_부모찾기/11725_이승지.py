from collections import deque

def bfs(start):
    dq = deque([start])
    visited[start] = 1

    while dq:
        now = dq.popleft()

        for next in tree[now]:
            if visited[next] == 0:
                visited[next] = now
                dq.append(next)

n = int(input())

# 연결리스트만들고임, 0은 무시
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

bfs(1)

print(*visited[2:], sep='\n')