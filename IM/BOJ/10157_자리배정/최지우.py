import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
K = int(input())

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cnt = 0
if K > R*C:
    print(0)
elif K == 1:
    print(1, 1)
else:
    while K > (R * 2 + C * 2) - 4:
        if R > 2 and C > 2:
            K -= (R * 2 + C * 2) - 4
            R -= 2
            C -= 2
            cnt += 1
    arr = [[-1] * C for _ in range(R)]

    now = (0, 0)
    d = 0
    arr[0][0] = K
    nx, ny = 0, 0
    while K > 1:
        x, y = now
        dx, dy = directions[d]
        nx, ny = x+dx, y+dy

        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == -1:
            K -= 1
            now = (nx, ny)
            arr[nx][ny] = K
        else:
            d += 1
            if d == 4:
                d = 0
        
    nx += 1 + cnt
    ny += 1 + cnt
    
    print(ny, nx)


'''
R
C-1
R-1
C-2
R-2
C-3
R-3
'''