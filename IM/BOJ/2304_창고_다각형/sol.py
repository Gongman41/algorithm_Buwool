import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()     # 기둥 위치 기준으로 정렬
max_height = max(data, key=lambda x: x[1])  # 높이를 기준으로
max_idx = data.index(max_height)    # 가장 높은 지점을 기준으로
result = 0

next = 1
now = 0
# 왼쪽부터 이동하면서, 나보다 큰 대상을 만날때까지 탐색
# 나보다 높은 대상을 만나면, 해당 대상위치와 내 위치 사이의 거리를 계산후,
# 내 높이만큼 곱한다. -> 내 높이 3, 내위치 1에서 상대위치 3까지거리 2 -> 총 6의 넓이
while next <= max_idx:
    if data[now][1] <= data[next][1]:
        result += (data[next][0] - data[now][0]) * data[now][1]
        now = next
        next += 1
    else:
        next += 1

# 위와 반대
next = N-2
now = N-1
while next >= max_idx:
    if data[now][1] <= data[next][1]:
        result += (data[now][0] - data[next][0]) * data[now][1]
        now = next
        next -= 1
    else:
        next -= 1
print(result + max_height[1])
