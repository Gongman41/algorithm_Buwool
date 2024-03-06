# import sys
# sys.stdin = open('input.txt')
r_five = [0]*5
l_five = [0]*5
lr_five = 0
rl_five = 0
val_idx_dict = {}
bingo_lst = []
cnt = 0
check = 0
for n in range(5):
    bingo_lst.append(list(map(int,input().split())))
    for m in range(5):
        val_idx_dict[bingo_lst[n][m]] = (n,m)

        
for n in range(5):
    temp = list(map(int,input().split()))
    for tem in temp:
        r,c = val_idx_dict[tem]
        r_five[r] += 1
        l_five[c] += 1
        if r == c:
            lr_five += 1
        if r == 4 - c:
            rl_five += 1
        cnt += 1
        
        if r_five[r] == 5:
            r_five[r] = 0
            check +=1
        if l_five[c] == 5:
            l_five[c] = 0
            check +=1
        if lr_five == 5:
            lr_five = 0
            check +=1
        if rl_five == 5:
            rl_five = 0
            check +=1
        if check >= 3:
            print(cnt)
            break
    if check >= 3:
        break