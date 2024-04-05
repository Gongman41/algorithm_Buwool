from heapq import heappush,heappop
def prim(start):
  pq = []
  MST = [0] * (N+1)
  # 최소 비용
  sum_weight = 0
  # 큐 비어있는 거에다 시작점 넣어놓고 빌때까지 반복
  # 기존에는 BFS 노드 번호만 관리
  # PRIM 우선순위가 가중치에 따라. 가중치가 낮으면 먼저 나와야됨
  # -> 관리해야할 데이터: 가중치, 노드번호_ 동시에 두가지 데이터 다루기
    # class로 만들거나 튜플로 만들기
    #  3가지 이상이 되면 class가 좋다
  heappush(pq,(0,start))
  while pq:
    weight, now = heappop(pq)
    # 방문했다면
    # 우선순위 큐 특성상 더 먼거리로 가는 방법이 큐에 저장이 되어 있기때문에 기존에 더 짧은 거리로 방문했다면 CONTINUE
    if MST[now]:continue
    MST[now] = 1
    sum_weight += weight
    # 갈 수 있는 노드들을 보면서
    for to in range(N+1):
      # 갈 수 없거나 이미 반복했다면
      if graph[now][to] == 0 or MST[to]:
        continue
      heappush(pq,(graph[now][to],to))
  print(sum_weight)
  
N = int(input())
M = int(input())

# 인접 행렬로 저장
# 실습 _ 인접 리스트로 저장
graph = [[0]* (N+1) for _ in range(N+1)]
for _ in range(M):
  s,e,w = map(int,input().split())

# 기존 3-> 4로 갈수 있다
# graph[3][4] = 1

# 가중치 그래프_ 3->4로 가는데 31이라는 비용이 든다
# graph[3][4] = 31
  graph[s][e] = w
  graph[e][s] = w

prim(1) 