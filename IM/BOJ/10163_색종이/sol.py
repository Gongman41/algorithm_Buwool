import sys
sys.stdin = open('input.txt')


N = int(input())
mat = [[0]*1003 for _ in range(1003)]
arr = [list(map(int, input().split())) for _ in range(N)]
count = [0] * N     # 종이마다 영역 표기 할것

for i in range(N):                          # 모든 색종이 순회 (종이 번호)
    a, b, w, h = arr[i]                     # 시작 좌표, 너비, 높이
    for x in range(a, a+w):                 # 시작점 + 너비, 시작점 + 높이 만큼 순회
        for y in range(b, b+h):
            if mat[x][y] != 0:              # 이전에 이미 붙인 종이가 있다면
                count[mat[x][y]-1] -= 1     # 이전에 붙인 종이의 영역의 넓이 -1
            mat[x][y] = i + 1               # 새 종이 붙이기 (종이 번호로 표시)
            count[i] += 1                   # 해당 번호의 영역 1 증가

for i in range(N):      # 0보다 작아진 (2번 이상 겹쳐져버려서 음수가 되버려도)
    print(count[i])

