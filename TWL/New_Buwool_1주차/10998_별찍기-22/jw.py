N = int(input())


'''
d: 방향 설정
    0: 왼쪽
    1: 아래
    2: 오른쪽
    3: 위로
    d += 1 해주고 % 4하면 순환 할듯 
'''
def star(x, y, d, c):
    global margin
    global fin
    if (x, y) == (row//2+1, col//2):
        fin = True
        return

    if fin:
        return

    if c == 0:
        c = 4
        margin += 2

    if d == 0:
        ny = y
        while ny != 0+margin:
            arr[x][ny] = '*'
            ny -= 1
        arr[x][ny] = '*'
        star(x, ny, (d+1)%4, c-1)
        return

    if d == 1:
        nx = x
        while nx != row-1-margin:
            arr[nx][y] = '*'
            nx += 1
        arr[nx][y] = '*'
        star(nx, y, (d+1)%4, c-1)
        return

    if d == 2:
        ny = y
        while ny != col-1-margin:
            arr[x][ny] = '*'
            ny += 1
        arr[x][ny] = '*'
        star(x, ny, (d+1)%4, c-1)
        return

    if d == 3:
        nx = x
        while nx != 0+margin:
            arr[nx][y] = '*'
            nx -= 1
        arr[nx][y] = '*'
        star(nx, y, (d+1)%4, c-1)
        return


if N == 1:
    print('*')
else:
    margin = 0
    col = (N-1)*4 + 1
    row = col + 2
    arr = [[' ']*col for _ in range(row)]
    fin = False

    star(0, col-1, 0, 3)

    for i in range(len(arr)):
        if i != 1:
            print(*arr[i], sep='', end='\n')
        else:
            print('*')