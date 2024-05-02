import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(start, now_dis):
    for a, b in graph[start]:
        if distance[a] == -1:   # 방문한 적 없다면!
            distance[a] = now_dis + b  # 현재까지의 거리 + 본인 가중치
            dfs(a, now_dis + b)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])   # 지름을 구할려면 반대로도 갈 수 있어야 하니까

# 총 2번의 dfs
# 1) 루트 노트에서 가장 멀리 있는 노드 찾기 (node a)
# 2) 1번에서 나온 노드에서 가장 멀리 있는 노드 찾기 (node b)
# => a, b 두 노드 사이의 거리가 지름이 됨

distance = [-1] * (n+1)
distance[1] = 0     # 시작 노드 distance는 0으로 초기화하고 시작
dfs(1, 0)
# print(distance)

node = distance.index(max(distance))     # 가장 멀리 있는 노드의 인덱스
distance = [-1] * (n+1)
distance[node] = 0
dfs(node, 0)
# print(distance)
print(max(distance))
