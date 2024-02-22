import sys
sys.stdin = open('input.txt')

arr= []
visit_x = [0] * 5
visit_y = [0] * 5
visit_d = []
visit_rd = []
d_chk = 0
rd_chk = 0

for i in range(5):
    line = list(map(int, input().split()))
    visit_d.append(line[i])
    visit_rd.append(line[4-i])
    arr.append(line)

bingo = 0
cnt = 0
for _ in range(5):
    call = list(map(int, input().split()))

    for i in call:
        cnt += 1
        if i in visit_d:
            d_chk += 1
            if d_chk == 5:
                bingo += 1
        if i in visit_rd:
            rd_chk += 1
            if rd_chk == 5:
                bingo += 1

        flag = False
        for x in range(5):
            for y in range(5):
                if arr[x][y] == i:
                    visit_x[x] += 1
                    visit_y[y] += 1

                    flag = True
                    if visit_x[x] == 5:
                        bingo += 1
                    if visit_y[y] == 5:
                        bingo += 1
                    break

            if flag:
                break

        if bingo >= 3:
            break

    if bingo >= 3:
        break
    
print(cnt)
