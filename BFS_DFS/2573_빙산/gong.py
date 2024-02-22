import sys
from collections import deque

sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
dr_r = [1, 0, -1, 0]
dr_c = [0, -1, 0, 1]
matrix = [[] for _ in range(N)]
l_v_cnt = 0 #중간에 갈 곳 다가면 탈출용
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

    l_v_cnt += M - matrix[i].count(0) #빙하개수 체크

year = 0
viewed = [[0] * M for _ in range(N)] # 시간 줄일려고 viewed 초기화안하고 밖으로 뺌.
while True:

    cnt = 0 #빙하 덩이
    c_v_cnt = 0 # 지금 간 빙하개수 체크. 위에껀 이전에 살아남은 빙하

    stack = deque()
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if matrix[i][j] > 0 and 0 <= viewed[i][j] < year + 1: #viewed 밖으로 빼고 요로코롬 처리
                cnt += 1
                viewed[i][j] += 1
                c_v_cnt += 1

                stack.append([i, j]) #스택처럼 보이지만 deque임
            while stack:
                count = 0
                star = stack.popleft()

                for n in range(4):
                    if 0 <= star[0] + dr_r[n] < N and 0 <= star[1] + dr_c[n] < M and matrix[star[0] + dr_r[n]][
                        star[1] + dr_c[n]] > 0 and 0 <= viewed[star[0] + dr_r[n]][star[1] + dr_c[n]] < year + 1:
                        # 빙하 높이 0보다 크고 아직 방문 안한곳
                        stack.append([star[0] + dr_r[n], star[1] + dr_c[n]])
                        viewed[star[0] + dr_r[n]][star[1] + dr_c[n]] += 1
                        c_v_cnt += 1

                    if 0 <= star[0] + dr_r[n] < N and 0 <= star[1] + dr_c[n] < M and matrix[star[0] + dr_r[n]][
                        star[1] + dr_c[n]] <= 0 and 0 <= viewed[star[0] + dr_r[n]][star[1] + dr_c[n]] < year + 1:
                        # 방문해서 바다가 된 빙하 빼고 순수 바다 체크. 0보다 작게한건 0으로 처리하기 귀찮아서 아예 빼버림
                        count += 1
                matrix[star[0]][star[1]] -= count
            if c_v_cnt == l_v_cnt: #긴급탈출
                break
        if c_v_cnt == l_v_cnt:
            break

    l_v_cnt = c_v_cnt  #마지막 빙하개수 갱신.

    if cnt == 1:
        year += 1
    else:
        break

if cnt == 1:
    print(0)
else:
    print(year)