import sys
sys.stdin = open('input.txt')

visited = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            if visited[y][x] == 0:
                cnt += 1
                visited[y][x] = 1
print(cnt)