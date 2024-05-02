import sys
sys.stdin = open('input.txt')

def dfs(start, now, cost, count):
    global min_cost
    if count == N and costs[now][start] != 0:   # 모든 도시를 방문했을 때 / 시작 도시로 돌아갈 수 있는지
        # 시작 도시로 돌아가는 비용을 포함하여 최소 비용 갱신
        min_cost = min(min_cost, cost + costs[now][start])
        return

    for i in range(N):
        # 아직 방문하지 않았고, 현재 도시에서 i 도시로 갈 수 있는 경우
        if not visited[i] and costs[now][i] != 0:
            visited[i] = 1
            dfs(start, i, cost + costs[now][i], count + 1)
            visited[i] = 0


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_cost = 1e9     # 최소 비용을 저장할 변수, 대충 큰 값으로 초기화

# 각 도시를 시작점으로 설정하여 DFS 탐색
for k in range(N):
    visited[k] = 1
    dfs(k, k, 0, 1)
    visited[k] = 0  # DFS 탐색이 끝난 후에는 현재 도시 i의 방문 상태를 다시 False로

print(min_cost)