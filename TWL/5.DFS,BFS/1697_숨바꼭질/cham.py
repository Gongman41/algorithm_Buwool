import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    q = deque([N])
    while q:
        now = q.popleft()
        if now == K:
            print(visited[now])
            break
        for next_node in (now + 1, now - 1, now * 2):   # 세 가지 선택지가 있음
            if 0 <= next_node < max_point and visited[next_node] == 0:
                visited[next_node] = visited[now] + 1   # visited 배열 통해서 시간을 구할 거야 ~
                q.append(next_node)

max_point = 100001
N, K = map(int, input().split())
visited = [0] * max_point
bfs()
