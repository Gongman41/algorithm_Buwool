import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
cnt = 0

d_list = deque()
y_list = deque()

for _ in range(N):
    d_list.append(input().strip())

for _ in range(N):
    y_list.append(input().strip())

while y_list:
    in_car = d_list[0]
    out_car = y_list.popleft()
    if in_car != out_car:   # in / out 차가 다르다면 (추월한 경우)
        cnt += 1
        d_list.remove(out_car)  # 추월한 차도 in_list에서 빼줌
    else:
        d_list.popleft()

print(cnt)




