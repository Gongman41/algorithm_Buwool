def ttt(arr):
    row = [''] * 3
    col = [''] * 3
    di = [''] * 2
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2]:
            if arr[i][0] == 'O':
                row[i] = 'O'
            elif arr[i][0] == 'X':
                row[i] = 'X'
        if arr[0][i] == arr[1][i] == arr[2][i]:
            if arr[0][i] == 'O':
                col[i] = 'O'
            elif arr[0][i] == 'X':
                col[i] = 'X'

    center = arr[1][1]
    if arr[0][0] == arr[2][2] == center:
        di[0] = center
    if arr[2][0] == arr[0][2] == center:
        di[1] = center
    return row, col, di


r1, r2 = 'invalid', 'valid'
while True:
    line = input().strip()
    if line == 'end':
        break

    x = line.count('X')
    o = line.count('O')
    # 개수비교
    if x < o or x > o+1:
        print(r1)
        continue

    arr = []
    if '.' in line:
        fin_check = False
    else:
        fin_check = True

    for i in range(3):
        arr.append(line[i*3:i*3+3])

    # x랑 o가 같으면, o가 두고 게임이 끝난 상태
    # 게임판에 빈 칸이 있어야 함
    if x == o:
        # 다 찼으면 불가능
        if fin_check:
            print(r1)
            continue
        # 가로, 세로, 대각선 이긴사람 있는지
        row, col, di = ttt(arr)
        # x가 이겼으면 X가 더 많아야 한다
        if 'X' in row+col+di:
            print(r1)
            continue
        # 빈 칸이 있는데, O가 이긴 줄이 없으면 불가능
        if 'O' not in row+col+di:
            print(r1)
            continue

        print(r2)
        continue
    # x가 하나 더 많은 상태
    # x가 이겼거나, 그냥 게임이 끝난 상태
    elif x == o + 1:
        row, col, di = ttt(arr)
        if not fin_check and 'X' not in row+col+di:
            print(r1)
            continue

        if 'O' in row+col+di:
            print(r1)
            continue

        print(r2)
        continue
    else:
        print(r1)

