from collections import deque


# 재귀~~ ㅎㅎ
def dfs(now):
    # 방문은 안했지만 들릴 수 있는 정점이니까 함수 들어왔을 거임 바로 visited 처리
    d_visited[now] = 1
    # 방금 방문했으니까 출력해욤
    print(now, end=' ')

    # 해당 정점과 연결된 정점들을 찾을 거야!
    for d_next in range(1, n + 1):
        # 해당 정점 row에서 각 index가 그 index에 해당하는 정점이 연결되어 있냐임
        # 1이라면 연결, 0이면 연결 안 되어 있다는 뜻
        if nodes[now][d_next] != 0:
            # 연결되어 있고 해당 정점을 아직 누구도 방문하지 않았다면
            if d_visited[d_next] == 0:
                # 해당 정점 기준으로 다시 탐색해요
                dfs(d_next)


def bfs(start):
    # 일단 시작점을 덱에 넣어욤
    dq = deque([start])
    # 넣으면서 바로 방문처리해야 손해가 적어요
    b_visited[start] = 1

    # 덱에 남은 것이 없을 때까지 반복문 돌아요
    while dq:
        # 맨 앞에 것을 빼서 bfs를 돌 거예욤
        now = dq.popleft()
        # 방문한 거니까 print
        print(now, end=' ')

        # 해당 정점과 연결된 정점들을 찾을 거야!
        for b_next in range(1, n + 1):
            # 해당 정점 row에서 각 index가 그 index에 해당하는 정점이 연결되어 있냐임
            # 1이라면 연결, 0이면 연결 안 되어 있다는 뜻
            if nodes[now][b_next] != 0:
                # 연결되어 있고 해당 정점을 아직 누구도 방문하지 않았다면
                if b_visited[b_next] == 0:
                    # 그 정점을 덱에 넣고
                    dq.append(b_next)
                    # 방문처리해요
                    b_visited[b_next] = 1
    # 내 마음 편하자고 넣었어요^^
    print()


n, m, v = map(int, input().split())
# 어떤 정점 번호는 1부터 n번까지니까~
nodes = [[0] * (n + 1) for _ in range(n + 1)]

# 인접 행렬을 만들어욤~
# 리스트를 만드니까 정점 번호가 작은 것부터 방문하도록 또 정렬해줘야했움
for _ in range(m):
    node1, node2 = map(int, input().split())
    # 양방향이니까 둘 다 넣어줘욤~
    # 둘 다 넣어줬지만 어차피 이미 갔으면 안 가겠지!
    nodes[node1][node2] = 1
    nodes[node2][node1] = 1

# dfs의 visited를 만들어욤
d_visited = [0] * (n + 1)
dfs(v)
print()

# bfs의 visited를 만들어욤
b_visited = [0] * (n + 1)
bfs(v)