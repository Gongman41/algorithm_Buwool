import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
# 면적 계산용 100 * 100 매트릭스
matrix = [[0] * 100 for _ in range(100)]
result = 0  # 누적 면적
for pos in data:    # 전체 좌표에 대해
    # 색종이는 항상 10 * 10
    for x in range(pos[0], pos[0] + 10):    # x ~ x + 10까지
        for y in range(pos[1], pos[1] + 10):    # y ~ y + 10까지
            if matrix[x][y] == 0:   # 2번 붙이는건 의미 없으므로 아직 안붙여진 곳에 대해서
                matrix[x][y] = 1    # 붙었다고 기록하고
                result += 1         # 면적 누적
print(result)