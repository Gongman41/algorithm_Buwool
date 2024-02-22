import sys
from collections import deque

# sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
dr_r = [1, 0, -1, 0]
dr_c = [0, -1, 0, 1]
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
year = 0
viewed = [[0] * M for _ in range(N)]
while True:

    cnt = 0

    stack = deque()
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if matrix[i][j] > 0 and 0 <= viewed[i][j] < year + 1:
                cnt += 1
                viewed[i][j] += 1

                stack.append([i, j])
            while stack:
                count = 0
                star = stack.popleft()

                for n in range(4):
                    if 0 <= star[0] + dr_r[n] < N and 0 <= star[1] + dr_c[n] < M and matrix[star[0] + dr_r[n]][
                        star[1] + dr_c[n]] > 0 and 0 <= viewed[star[0] + dr_r[n]][star[1] + dr_c[n]] < year + 1:
                        stack.append([star[0] + dr_r[n], star[1] + dr_c[n]])
                        viewed[star[0] + dr_r[n]][star[1] + dr_c[n]] += 1

                    if 0 <= star[0] + dr_r[n] < N and 0 <= star[1] + dr_c[n] < M and matrix[star[0] + dr_r[n]][
                        star[1] + dr_c[n]] <= 0 and 0 <= viewed[star[0] + dr_r[n]][star[1] + dr_c[n]] < year + 1:
                        count += 1
                matrix[star[0]][star[1]] -= count

    if cnt == 1:
        year += 1
    else:
        break

if cnt == 1:
    print(0)
else:
    print(year)