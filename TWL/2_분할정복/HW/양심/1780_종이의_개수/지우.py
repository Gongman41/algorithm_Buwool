import sys
input = sys.stdin.readline


def paper(N, x, y):
    global result

    color = arr[x][y]
    if N == 1:
        result[color] += 1
        return
    
    flag = True
    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j] != color:
                flag = False
                break
        if not flag:
            break

    
    if flag:
        result[color] += 1
    else:
        for dx in range(x, x+N, N//3):
            for dy in range(y, y+N, N//3):
                paper(N//3, dx, dy)
    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]
paper(N, 0, 0)
for i in (-1, 0, 1):
    print(result[i])