import sys
sys.stdin = open('input.txt')


R, C = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x : x[1])
# (가로 시작, 종료), (세로 시작, 종료)
paper = [[(0, R)], [(0, C)]]
# 자른다.
for cut in arr:
    # 방향, 자를 지점
    d, pos = cut[0], cut[1]
    if d == 0:
        piece = paper[1].pop()
        paper[1].append((piece[0], pos))
        paper[1].append((pos, piece[1]))
    else:
        piece = paper[0].pop()
        paper[0].append((piece[0], pos))
        paper[0].append((pos, piece[1]))
result = 0
# 모든 종이 좌표 구해놨으니, 모든 경우 넓이 계산하기
for x in paper[0]:
    for y in paper[1]:
        if result < (x[1] - x[0]) * (y[1] - y[0]):
            result = (x[1] - x[0]) * (y[1] - y[0])
print(result)