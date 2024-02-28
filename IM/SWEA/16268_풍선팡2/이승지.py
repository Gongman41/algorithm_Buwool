# import sys
# sys.stdin = open("input1.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    pang = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    max_remove = 0
    for i in range(n):
        for j in range(m):
            current_remove = pang[i][j]
            for d in range(4):
                ni = di[d] + i
                nj = dj[d] + j

                if 0 <= ni < n and 0 <= nj < m:
                    current_remove += pang[ni][nj]

            if current_remove > max_remove:
                max_remove = current_remove

    print(f'#{test_case} {max_remove}')
