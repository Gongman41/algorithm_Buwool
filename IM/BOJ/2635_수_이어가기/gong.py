# import sys
# sys.stdin = open('input.txt')
N = int(input())
n_list = []
max_cnt = 0
for n in range(1,N+1):
    temp = [N]
    a = n
    cnt = 1
    while a >= 0:
        temp.append(a)
        cnt += 1
        a = temp[-2] - temp[-1]
    if max_cnt < cnt:
        max_cnt = cnt
        n_list = temp
print(max_cnt)
print(*n_list)
    
        
        
        