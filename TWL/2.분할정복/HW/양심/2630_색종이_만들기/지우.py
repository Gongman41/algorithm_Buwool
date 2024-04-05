import sys
input = sys.stdin.readline


def pp(x, y, N):
    global b, w

    color = P[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != P[i][j]:
                pp(x, y, N//2)
                pp(x, y+N//2, N//2)
                pp(x+N//2, y, N//2)
                pp(x+N//2, y+N//2, N//2)
                return
    if color == 0: w +=1
    else: b+= 1


N = int(input())

P = [list(map(int, input().split())) for _ in range(N)]

b, w = 0, 0
pp(0, 0, N)

print(w, b, sep='\n')