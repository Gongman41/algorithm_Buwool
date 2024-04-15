from collections import deque

# 최단거리니까 bfs
# 만약 서로 다른 경로가 같은 칸을 지나려고 할 때에도 bfs에 의해
# 먼저 도착한 칸(이동 거리가 짧은)을 기준으로 이미 거리를 계산(miro값 변경)했기 때문에
# 딱히 조건을 주지 않아도 된다.
def bfs(start):
    dq = deque([start])

    while dq:
        now = dq.popleft()

        for d in range(4):
            ni = now[0] + di[d]
            nj = now[1] + dj[d]
            if 0 <= ni < n and 0 <= nj < m:
                # 갈 수 있는 좌푯값이 1이면 가도 됨
                # 0이면 원래 못가고 2이상이면 이미 최단거리로 방문한 곳
                # 근데 시작 좌표로 다시 돌아가서는 안 되지요
                if miro[ni][nj] == 1 and (ni != 0 or nj != 0):
                    # 최단 이동거리로 miro값 변경
                    miro[ni][nj] = miro[now[0]][now[1]] + 1
                    dq.append([ni, nj])

n ,m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

# 인접한 칸에 1이 있으면 일단 갈 수는 있으니까 델타 탐색을 위한 좌표값을 넣어준다
di = [0,0,1,-1]
dj = [1,-1,0,0]

# 시작좌표가 [0,0]이고 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어지니까
# bfs에서 덱에 아무것도 없을 때까지 탐색한다
bfs([0,0])
# 해당 칸으로 이동하기 위해 지나야 하는 최소 칸 수를 miro 값을 바꾸며 계산해주어서
# 그냥 miro에 있는 [n-1, m-1]의 값을 보면 됨
print(miro[n-1][m-1])