import sys
sys.stdin = open('input.txt')
T = int(input())
def checking_RC(r,c):
    global count
    count += 1
    r_len = 0
    c_len = 0
    while r+r_len != N-1 and matrix[r+r_len][c] != 0:
        r_len += 1
    while c+c_len != N-1 and matrix[r][c+c_len] != 0:
        c_len += 1
    for i in range(r,r+r_len+1):
        for j in range(c, c+c_len + 1):
            matrix[i][j] = 0
    return [r_len, c_len, r_len*c_len]

for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    lst = []
    for rr in range(N):
        for cc in range(N):
            if matrix[rr][cc]:
                lst.append(checking_RC(rr,cc))
    lst.sort(key = lambda x:x[2])
    for ls in range(len(lst)-1):
        if lst[ls][2] == lst[ls+1][2]:
            if lst[ls][0] > lst[ls+1][0]:
                lst[ls],lst[ls+1] = lst[ls+1],lst[ls]


    print(f'#{tc} {count} ',end='')
    for l in range(len(lst)):
        print(lst[l][0],end=' ')
        print(lst[l][1],end=' ')
    print()







