import sys
sys.stdin = open('input.txt')

def Russian(row, color, ans):
    global result
    
    if ans >= result:
        return
    elif row == N-1:
        result = ans
        return
    else:
        tmp = M-cnt[color][row-1]
        if row + 1 >= N-2 and color == 1:
            # print(row, color)
            # print(ans, tmp)
            # print('------')
            Russian(row+1, color+1, ans+tmp)
        else:
            # print(row, color)
            # print(ans, tmp)
            # print('------')
            Russian(row+1, color, ans+tmp)
            if color != 3:
                Russian(row+1, color+1, ans+tmp)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    WnR = 0
    cnt = {1: [], 2: [], 3: []}

    for i in range(N):
        Wcnt = Bcnt = Rcnt =0
        for j in range(M):
            if i == 0 and arr[i][j] != 'W':
                WnR += 1
            elif i == N-1 and arr[i][j] != 'R':
                WnR += 1
            else:
                if arr[i][j] == 'W':
                    Wcnt +=1
                elif arr[i][j] == 'B':
                    Bcnt +=1
                else:
                    Rcnt += 1
        if i != 0 and i != N-1:
            cnt[1].append((Wcnt))
            cnt[2].append((Bcnt))
            cnt[3].append((Rcnt))
    
    result = N*M
    Russian(1, 1, 0)
    Russian(1, 2, 0)
    print(f'#{tc} {WnR + result}')
'''
1 1 > 2 2
1 2 > 2 2
1 2 > 2 3

WBRR
BRRR
BBRR


#1 1 1, 2 1, 3 1, 4 2
#2 1 1, 2 1, 3 2, 4 2
#3 1 1, 2 1, 3 2, 4 3
#4 1 1, 2 2, 3 2, 4 2
#5 1 1, 2 2, 3 2, 4 3
#6 1 1, 2 2, 3 3, 4 3
#7 1 2, 2 2, 3 2, 4 2
#8 1 2, 2 2, 3 2, 4 3
#9 1 2, 2 2, 3 3, 4 3
#10 1 3, 2 3, 3 3, 4 3
'''