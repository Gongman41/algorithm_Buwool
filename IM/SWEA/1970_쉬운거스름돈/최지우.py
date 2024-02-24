import sys
sys.stdin = open('input.txt')

c_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, int(input())+1):
    m = int(input())
    print(f'#{tc}')
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(c_lst)):
        if m//c_lst[i] > 0:
            result[i] += m//c_lst[i]
            m %= c_lst[i]
            
    print(*result)