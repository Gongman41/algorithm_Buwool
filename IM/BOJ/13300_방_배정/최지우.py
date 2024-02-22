import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
student = {i:[0, 0] for i in range(1, 7)}
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        student[Y][0] += 1
    else:
        student[Y][1] += 1

cnt = 0
for w, m in student.values():
    w -= 1
    m -= 1
    cnt += (w//K) + (m//K) + 2
print(cnt)

