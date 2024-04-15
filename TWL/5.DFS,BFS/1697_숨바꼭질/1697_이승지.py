from collections import deque

# 최단거리니까 bfs로 풀어봤음요..!
def bfs(start):
    dq = deque([start])
    visited[start] = 0

    while dq:
        now = dq.popleft()

        if now == k:
            return visited[k]

        for i in range(3):
            next = move[i](now)
            if 0 <= next <= 100000:
                if visited[next] == -1:
                    dq.append(next)
                    visited[next] = visited[now] + 1


n, k = map(int, input().split())

move = [lambda x: x - 1, lambda x: x + 1, lambda x: x * 2]

min_sec = float('inf')
# 갈 수 있는 칸
visited = [-1] * 100001
print(bfs(n))
