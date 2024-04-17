import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

def bfs(i):
    check[i] = 1  # check에는 1 or -1 넣어줌
    q = deque([i])
    while q:
        now = q.popleft()
        for next_node in adj_list[now]:
            if not check[next_node]:    # 값이 없으면(0이라면)
                check[next_node] = -(check[now])
                q.append(next_node)
            else:   # 값이 있는 경우
                if check[next_node] == check[now]:  # check 값이 같다면
                    return False
    else:
        return True

T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    check = [0] * (V+1)

    # bfs() -> bfs로 풀 때 비연결 그래프일 경우 모든 정점을 탐색해 줘야 해서 이래 하면 안됨!!!
    for i in range(1, V+1):
        if check[i] == 0:
            result = bfs(i)
            if result == 0:
                print('NO')
                break
    else:
        print('YES')


