import sys

sys.stdin = open('input.txt')


def bomb(sibal):
    global cnt
    new_lst = []
    dx = [0, 1, 0, -1]  # 오른쪽 아래 왼쪽 위
    dy = [1, 0, -1, 0]  # 우 하 좌 상
    for a in range(N):
        for b in range(N):
            if visited[a][b] == 0 and sibal[a][b] != 0:
                cnt += 1
                i = a
                j = b
                stack = [(i, j)]
                stackkk = [(i, j)]
                garo = 1
                visited[i][j] = 1
                while stack:
                    nx, ny = stack.pop()
                    for k in range(4):
                        cx = nx + dx[k]
                        cy = ny + dy[k]

                        if 0 <= cx < N and 0 <= cy < N and visited[cx][cy] == 0 and sibal[cx][cy] != 0:
                            stack.append((cx, cy))
                            stackkk.append((cx, cy))
                            visited[cx][cy] = 1
                        if j == cy:
                            garo += 1
                min_x, min_y = min(stackkk)
                max_x, max_y = max(stackkk)
                garo = max_x - min_x + 1
                sero = max_y - min_y + 1
                nulbi = garo * sero
                new_lst.append([nulbi, garo, sero])

                # print('넓이다임마', len(stackkk))
    new_lst.sort()
    return new_lst


T = int(input())
for tc in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    # print(visited)
    result = bomb(lst)
    print(f'#{tc}', cnt, end=' ')
    for i in range(cnt):
        print(*result[i][1:3], end=' ')
    print()
