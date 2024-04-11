# import sys
# from collections import deque
# K = int(input())
# for _ in range(K):
#     V,E = map(int,input().split())
#     graph = [[] for _ in range(V+1)]
#     visited = [0]*(V+1)
#     for _ in range(E):
#         u,v = map(int,sys.stdin.readline().split())
#
#         graph[min(u,v)].append(max(u,v))
#
# #     bfs로 순회하다가... 부모에서 오는 간선이랑 형제끼리 간선 구분 어떻게.
# # level로 계산? 아 유니온 파인드
#
#     deq = deque([1])
#     visited[1] = 1
#     while deq:
#         cur = deq.popleft()
#         if visited[cur] ==1:
#             print('NO')
#             break
#         visited[cur] = 1
#         if graph[cur]:
#             for i in graph[cur]:
#                 deq.append(i)
#     else:
#         print('YES')

import sys
sys.setrecursionlimit(10**6)
k = int(input())


def DFS(start, visited, graph, group):
    visited[start] = group  # 현재 노드의 그룹 저장

    # 인접 노드 탐색
    for v in graph[start]:
        if visited[v] == 0:  # 아직 방문하지 않은 노드
            # -group : 현재 노드의 그룹과 다른 값 전달
            result = DFS(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:  # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
                return False
    return True


for _ in range(k):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            result = (DFS(i, visited, graph, 1))
            if not result:
                break
    print("YES") if result else print("NO")






