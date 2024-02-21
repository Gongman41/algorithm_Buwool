import sys
sys.stdin = open('input.txt')


# 하 좌 우하 좌하
dir = [(1, 0), (0, 1), (1, 1), (1, -1)]

def check(x, y, d):
    '''
        아래로 조사한다면, 아래 조사 시작지점 좌표를
        (0, y)로 초기화
        빙고는 무작위 위치의 번호가 불리므로, 해당 줄 세로줄의
        빙고 여부를 파악하려면 해당 줄의 제일 위부터 빙고가 가능한지 체크 하여야함
    '''
    if d == 0: nx, ny = 0, y
    elif d == 1: nx, ny = x, 0  # 가로 조사도 마찬가지
    elif d == 2:    # 우하 대각선 조사의 경우
        if x != y: return False # 좌표가 (0,0) (1,1) 등으로 증가할 것
        # 그렇다면 0,0 부터 조사할 수 있도록 초기화
        nx, ny = 0, 0
    else:
        # 좌하 대각선은 두 좌표의 합이 4 (0, 4) (1, 3) 일때만
        if x + y != 4: return False
        # 우측 최상단 좌표로 초기화
        nx, ny = 0, 4

    while 0 <= nx < 5 and 0 <= ny < 5:
        if arr[nx][ny] != -1:
            return False
        nx += dir[d][0]
        ny += dir[d][1]
    return True

# 빙고판 입력
arr = [list(map(int, input().split())) for _ in range(5)]
# 각 숫자가 작성된 좌푯값 기록
# 예제에서 11은 0,0 이었음.
# pos = {11: (0, 0)
pos = {arr[x][y]: (x, y) for y in range(5) for x in range(5)}

cnt = 0
bingo = []
# 5*5에 대한 전수 조사
for i in range(5):  # 0 ~ 5
    # 사회자가 부르는 번호: 5개씩 5줄 idx -> 1 ~ 5 (i번째 줄의 idx번째 값)
    # 따라서 i*5 + idx 번째 번호가 될 것
    for idx, num in enumerate(list(map(int, input().split())), 1):
        # 세로, 가로, 우하대각선, 좌하대각선에 대해 빙고여부 체크
        checkList = [0, 0, 0, 0]
        x, y = pos[num] # 사회자가 부른 번호를 내 빙고판 어느 좌표에 기록했는지 확인
        arr[x][y] = -1  # 해당 위치 번호 -1로 초기화 (체크하였음)
        for k in range(4):  # 4방향에 대해 조사
            checkList[k] = check(x, y, k)
        # 이번 번호에 대해 상하대각선 빙고 여부 파악후
        if any(checkList):  # checkList에 하나라도 1이 있다면, (한줄이라도 빙고가 되었다면)
            cnt += checkList.count(True)    # 빙고된 줄의 수 덧셈
            # 굳이 매번 checkList에 모든 방향에 대한 전수조사를 하는 이유는,
            # 특정 번호를 체크한 순간, 가로, 세로가 동시에 빙고가 되는 경우가 있을 수 있음
        if cnt >= 3:
            print(i*5 + idx)
            break
    if cnt >= 3:
        break
