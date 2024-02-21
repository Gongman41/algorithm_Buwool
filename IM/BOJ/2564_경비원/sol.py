import sys
sys.stdin = open('input.txt')

# 아래로 가는 경우 -, 오른쪽으로 가는 경우 +
'''
0  → +
↓  - - -
-  |   |
   |   |
   - - -
'''
def search(a):  # 원점(왼쪽 위)과의 최단거리를 구하는 함수
    if a[0] == 1:  # 북쪽
        return a[1]
    if a[0] == 2:  # 남쪽
        return -(C + a[1])
    if a[0] == 3:  # 서쪽
        return -a[1]
    if a[0] == 4:  # 동쪽
        return R + a[1]

R, C = map(int, input().split())  # 가로, 세로 입력
N = int(input())  # 상점 개수
arr = []
for _ in range(N):  # 상점과 원점과의 거리 저장
    arr.append(search(list(map(int, input().split()))))
dg = search(list(map(int, input().split())))  # 경비원과 원점과의 거리
length = 2 * R + 2 * C
min_len = 0
for i in arr:  # 상점과 경비원의 거리는 |dg-i| 와 length - |dg-i| 두개가 된다
    n = abs(dg - i)
    if n >= length - n:
        min_len += length - n
    else:
        min_len += n
print(min_len)