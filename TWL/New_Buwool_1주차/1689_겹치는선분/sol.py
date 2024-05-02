import sys
sys.stdin = open('input.txt')

'''
1차원 좌표계 위에 선분 N개
최대로 겹친 선분의 개수를 구해보자.
첫째줄에 100만개의 선분
그다음 N개의 줄에 선분의 시작좌표와 끝나는 좌표 e(s<e)
선분의 좌표는 절대값이 10억보다 작거나 같은 정수이다.
1. 그럼 왼쪽 좌표 기준 정렬
2. 선분의 끝 점에서 겹치는 것은 겹치는 것으로 세우지 않음
그럼 선분의 끝에 겹치는지 안겹치는지가 중요하다
그럼 첫 시작점들로만 정렬을 시킨후에,
시작점에 +1 을 주고, 끝점에 -1을 주면 누적합하게 된다.
'''

N = int(input()) # 선분의 개수
area = []
for _ in range(N):
    start, end = map(int,input().split())
    area.append((end,-1))
    area.append((start,1))
area.sort()
for i in range(1,N):
    if area[i][0] == area[i-1][0] and area[i][1] != area[i][1]:
        area.pop(i)
        area.pop(i-1)

sumi = 0
result = 0
for a, b in area:
    sumi += b
    result = max(result, sumi)
print(result)