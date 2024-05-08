import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

def dfs(start, distance):
    for next, next_d in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + next_d
            dfs(next, distance + next_d)


visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

last_Node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[last_Node] = 0
dfs(last_Node, 0)

print(max(visited))