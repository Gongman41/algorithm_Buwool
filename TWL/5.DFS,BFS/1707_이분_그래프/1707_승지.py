from collections import deque

def bfs(start):
    dq = deque([start])
    visited[start] = 1

    while dq:
        now = dq.popleft()

        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = 3 - visited[now]
                dq.append(next)
            elif visited[next] != visited[now]:
                continue
            else:
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    # 인접리스트데이, 1부터 들어가니까 0은 무시
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    # visited_all = [1] * v
    # visited_all.insert(0, 0)
    # # 모든 노드가 이어져 있지 않을 수도 있음 !! 비연결 그래프일 수도 있다는 말
    # # 다 돌면 시간이 넘 오래 거릶! !! @  각 그래프마다 대표하는 거 하나 찾아볼까나
    # for i in range(1, v+1):
    #     visited = [0] * (v+1)
    #     if visited == visited_all:
    #         print("YES")
    #         break
    #     if not bfs(i):
    #         print("NO")
    #         break
    # else:
    #     print("YES")

    parents = [i for i in range(v+1)]  # 대표 원소 배열

    def find_set(x):
        if parents[x] == x:
            return x
        # 집합 찾으면서 갱신하여 대표 원소를 빠르게 찾도록 함 -> 경로 압축
        # 직전 부모(?)나 연결 정보는 사라짐
        parents[x] = find_set(parents[x])
        return parents[x]

    def union(a, b):
        x = find_set(a)
        y = find_set(b)

        if x == y:
            return

        # 더 작은 루트노드에 합친다(최소 간선 방문도 중요하니께 -> 가중치에 영향)
        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    # 모든 노드가 이어져 있지 않을 수도 있음 !! 비연결 그래프일 수도 있다는 말
    # 다 돌면 시간이 넘 오래 거릶! !! @  각 그래프마다 대표하는 거 하나 찾아볼까나
    for node1 in range(1,v+1):
        for node2 in graph[node1]:
            if find_set(node1) != find_set(node2):
                union(node1, node2)

    for i in set(parents):
        visited = [0] * (v + 1)
        if not bfs(i):
            print("NO")
            break
    else:
        print("YES")