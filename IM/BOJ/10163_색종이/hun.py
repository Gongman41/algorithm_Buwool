import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []
for _ in range(N):
    x, y, garo, sero = map(int, input().split())
    lst.append((x, y, garo, sero))

visited = [[0]*1001 for _ in range(1001)]
result = []
while lst:
    cnt = 0
    x, y, garo, sero = lst.pop()
    for i in range(y, y+sero):
        for j in range(x, x+garo):
            if visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1
    result.append(cnt)
for aaa in result[::-1]:
    print(aaa)
