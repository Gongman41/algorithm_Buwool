import sys
input = sys.stdin.readline

N = int(input())
t = [list(map(int, input().split())) for _ in range(N)]
t.sort(key=lambda x: (x[1], x[0]))

cnt = 0
cur = 0
for meet in t:
    start, end = meet
    if cur <= start:
        cnt += 1
        cur = end

print(cnt)