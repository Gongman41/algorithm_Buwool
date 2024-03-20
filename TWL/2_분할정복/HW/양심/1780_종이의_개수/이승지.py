def sol(paper, size, cnt):
    gijun = paper[0][0]

    first_rule = True
    for i in range(size):
        for j in range(size):
            if paper[i][j] != gijun:
                first_rule = False
                break
        if not first_rule:
            break

    if not first_rule:
        for n in range(0, size, size // 3):
            for m in range(0, size, size // 3):
                new_matrix = []
                for ii in range(size // 3):
                    new_row = []
                    for jj in range(size // 3):
                        ni = n + ii
                        nj = m + jj
                        new_row.append(paper[ni][nj])
                    new_matrix.append(new_row)
                sol(new_matrix, size // 3, cnt)

    else:
        cnt[gijun + 1] += 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = [0] * 3
sol(matrix, n, cnt)
for c in range(3):
    print(cnt[c])
