import sys
sys.stdin = open('input.txt')


mx_x = mx_y = 0

sq = []
for _ in range(4):
    x, y, X, Y = map(int, input().split())
    mx_x = max(mx_x, X)
    mx_y = max(mx_y, Y)
    sq.append((x, y, X, Y))

arr = [[0] * mx_x for _ in range(mx_y)]

ans = 0
for n in sq:
    x, y, X, Y = n
    for i in range(y, Y):
        for j in range(x, X):
            if arr[i][j] == 0:
                arr[i][j] = 1
                ans += 1

print(ans)
