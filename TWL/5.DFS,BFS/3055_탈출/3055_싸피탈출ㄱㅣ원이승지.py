from collections import deque

def find_all():
    global init_water, s, d

    for i in range(r):
        for j in range(c):
            # 물이 차 있는 곳 하나라고 한 적 없음~~
            if maps[i][j] == '*':
                init_water.append((i, j))
            if maps[i][j] == 'S':
                s = (i, j)
            if maps[i][j] == 'D':
                d = (i, j)


def bfs():
    # 하나의 덱에 넣어도 물 조건 먼저 따지고 고슴도치 이동 조건 따질 거고 넣은 순서대로 popleft하니까
    # n분 후 일어나는 상황에 대한 순서 보장이 가능함
    dq = deque([])
    # water과 고슴도치 이동 좌표를 각자 구분하기 위한 문자 하나 추가
    for water in init_water:
        dq.append((water, 'W'))
    dq.append((s, 'S'))
    # 큰 while문 한 번 돌고 나면 1분이 지난 거니까 굳이 visited나 maps에 직접 조작을 가하지 않아도 이렇게 가장 빠른 시간을 계산 할 수 있따
    time = 0

    while dq:
        for _ in range(len(dq)):
            pos, t = dq.popleft()
            # 초기에 물이 차있지 않을 수도 있따? 그럼 빈 튜블이라서 에러 뜸
            if pos:
                if t == 'W':
                    for i in range(4):
                        w_next_r, w_next_c = pos[0] + di[i], pos[1] + dj[i]
                        if 0 <= w_next_r < r and 0 <= w_next_c < c:
                            if maps[w_next_r][w_next_c] == '.' or maps[w_next_r][w_next_c] == 'S':
                                # S를 바꿔도 되는 이유는 어차피 앞 전 순서에서 S의 좌표를 dq에 넣어놔서 고슴도치 이동은 잘 고려할 수 있음
                                # 바꾸지 않고 그냥 dq에만 넣으면 dq가 끝나질 않는다...
                                maps[w_next_r][w_next_c] = '*'
                                dq.append(((w_next_r, w_next_c), 'W'))
                elif t == 'S':
                    for i in range(4):
                        d_next_r, d_next_c = pos[0] + di[i], pos[1] + dj[i]
                        if 0 <= d_next_r < r and 0 <= d_next_c < c:
                            # 현재를 기준으로 D를 따지면 더 돌아야하니까 next 기준으로 D에 도착한지 따져본다
                            if maps[d_next_r][d_next_c] == 'D':
                                return time + 1
                            if maps[d_next_r][d_next_c] == '.':
                                maps[d_next_r][d_next_c] = 'S'
                                dq.append(((d_next_r, d_next_c), 'S'))
        time += 1

    return "KAKTUS"


r, c = map(int, input().split())
maps = [list(char for char in input() if char != ' ') for _ in range(r)]
# strip()은 양끝만 봄
# 중간에 공백 들어가는 상황도 생각해야하네...?

init_water = []
s = ()
d = ()

find_all()

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

result = bfs()
print(result)
