import sys
sys.stdin = open('input.txt')
N = int(input())
dice_lst = [list(map(int,input().split())) for _ in range(N)]
max_n = 0
dice_dict = {0:5,1:3,2:4,4:2,3:1,5:0}
for start in range(6):
    cur = 6
    if dice_lst[0][start] == 6 or dice_lst[0][dice_dict[start]] == 6:
        cur = 5
    value = dice_lst[0][start]
    for n in range(1,N):
        tem_max = dice_lst[n][:] # 얕은 복사
        idx = tem_max.index(value)

        tem_max[idx] = 0
        value = tem_max[dice_dict[idx]]
        tem_max[dice_dict[idx]] = 0

        cur += max(tem_max)
    max_n = max(max_n,cur)
print(max_n)

# 0 5 1 3 2 4

