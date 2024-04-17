# from collections import deque
# 인접한 접점의 색이 다른 그래프
# N,K = map(int,input().split())
# deq = deque([])
# deq.append([N,0])
# visited = [0]*100001
# visited[N] = 1
# min_time = 10e10
# while deq:
#     cur,time = deq.popleft()
#     if cur == K:
#         min_time = min(time,min_time)
#         continue
#     if time >= min_time:
#         continue
#     if 0 <= cur + 1 <= 100000 and visited[cur+1]==0:
#         deq.append([cur+1,time+1])
#         visited[cur+1] = 1
#     if 0 <= cur -1 <= 100000 and visited[cur-1]==0:
#         deq.append([cur-1,time+1])
#         visited[cur-1] = 1
#     if 0<= 2*cur <= 100000 and visited[2*cur] == 0:
#         deq.append([2*cur,time+1])
#         visited[2*cur] = 1
# print(min_time)

# from collections import deque

# k = int(input())


# def bfs(graph, start):
#     queue = deque()
#     queue.append(start)
#     if visited[start] == 0:
#         visited[start] = 1  # 이분은 1, 2로 하고 아직 방문하지 않은곳은 0으로 표시
#     while queue:
#         v = queue.popleft()

#         color = visited[v]
#         for i in graph[v]:  # V정점과 연결된 모든 정점 확인
#             if visited[i] == 0:  # 아직 한번도 방문하지 않음
#                 queue.append(i)  # 다음에 방문할 곳으로 지정
#                 if color == 1:  # 현재의 정점과 다른 색상으로 색칠
#                     visited[i] = 2
#                 else:
#                     visited[i] = 1
#             elif visited[i] == 1:
#                 if color == 1:
#                     print("NO")
#                     return False
#             elif visited[i] == 2:
#                 if color == 2:
#                     print("NO")
#                     return False
#     return True


# for i in range(k):
#     flag = 0
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V + 1)]
#     visited = [0] * (V + 1)
#     for j in range(E):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     for k in range(1, V + 1): # 연결그래프일 경우에는 시작점에서 한번의 BFS를 수행하면 되지만 비연결그래프의 경우에는 모든 정점을 탐색해야 한다.
#         if not bfs(graph, k):
#             flag = 1
#             break
#     if flag == 0:
#         print("YES")

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

