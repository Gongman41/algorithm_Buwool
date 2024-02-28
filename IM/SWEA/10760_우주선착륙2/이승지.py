# import sys
# sys.stdin = open("input2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    height = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 0, 1, -1, 1, 1, -1, -1]
    dj = [1, -1, 0, 0, 1, -1, 1, -1]

    candidate = 0
    for i in range(n):
        for j in range(m):
            standard = height[i][j]
            count = 0
            for d in range(8):
                if count >= 4:
                    break

                ni = di[d] + i
                nj = dj[d] + j

                if 0 <= ni < n and 0 <= nj < m:
                    if height[ni][nj] < standard:
                        count += 1

            if count >= 4:
                candidate += 1

    print(f'#{test_case} {candidate}')
