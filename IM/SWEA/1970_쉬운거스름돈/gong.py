import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    guth_list = [50000,10000,5000,1000,500,100,50,10]
    count_list = [0]*8
    for i in range(len(guth_list)):
        count_list[i] = N//guth_list[i]
        N %= guth_list[i]
    print(f'#{tc} ')
    print(*count_list)