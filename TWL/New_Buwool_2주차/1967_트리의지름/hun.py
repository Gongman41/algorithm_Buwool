import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, w = map(int, input().split())
    tree[n1].append([n2, w])
    tree[n2].append([n1, w])
# print(tree)
visited = [-1]*(n+1)
visited[1] = 0


def dfs(x, w):
    for i in tree[x]:
        a, b = i
        if visited[a] == -1:
            visited[a] = w + b
            dfs(a, w + b)


dfs(1, 0)
start = visited.index(max(visited))
# print(start)
visited = [-1]*(n+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))