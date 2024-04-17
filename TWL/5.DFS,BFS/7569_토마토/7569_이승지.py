from collections import deque

def bfs():
    global dq
    cnt = 0

    while dq and tomatoes != all_ripe:
        for _ in range(len(dq)):
            now = dq.popleft()

            for same_h in range(4):
                ni, nj = now[1] + di[same_h], now[2] + dj[same_h]
                if 0 <= ni < n and 0 <= nj < m:
                    # visited 상관 없는 듯? 왜냐면... 0인데 방문하면 1로 바로 바꾸고 0인 것만 들어가니까 1인건 이미 방문한ㄱ거잖아
                    # 바꿀 거 다 바꿔도 dq에는 마지막에 바꾼 것들 남아있음~~ 걔네들도 옆에 토마토를 익게 만들고 싶어 ^^
                    # 근데 이제 더이상 익게 만들 게 없으니까.. cnt를 해서는 안 되겠지? 그래서 while문 조건을 이렇게 주는 거임
                    # visited랑은 상관없음 걔네는 익게하는 조건을 안 따진 건 맞아요(이제 필요가 없어진 것 뿐)
                    if tomatoes[now[0]][ni][nj] == 0:
                        tomatoes[now[0]][ni][nj] = 1
                        dq.append((now[0],ni,nj))

            for diff_h in range(2):
                nk = now[0] + dk[diff_h]
                if 0 <= nk < h:
                    if tomatoes[nk][now[1]][now[2]] == 0:
                        tomatoes[nk][now[1]][now[2]] = 1
                        dq.append((nk, now[1], now[2]))
        cnt += 1
    return cnt

# 상자의 가로 세로 상자의수
m,n,h = map(int, input().split())

tomatoes = []
all_ripe = []
dq = deque([])

di = [0,0,1,-1]
dj = [1,-1,0,0]
dk = [-1,1]

for k in range(h):
    original_h = []
    changed_h = []
    for i in range(n):
        col = list(map(int, input().split()))
        original_h.append(col)

        changed_h.append(col[:])
        for j in range(m):
            if original_h[i][j] == 1:
                dq.append((k, i, j))
            if original_h[i][j] == 0:
                changed_h[i][j] = 1
    tomatoes.append(original_h)
    all_ripe.append(changed_h)

time = bfs()
if tomatoes == all_ripe:
    print(time)
else:
    print(-1)
