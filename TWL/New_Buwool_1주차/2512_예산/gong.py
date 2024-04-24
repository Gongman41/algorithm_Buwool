import sys

# # 재귀 호출의 깊이 한계를 늘림
sys.setrecursionlimit(10 ** 8)
N = int(input())
n_lst = list(map(int,input().split()))
M = int(input())
# 이분탐색. 카운팅소트. 합계값
min_n = 10e10
max_n = 0
bestMoney = 0
for i in range(N):
    min_n = min(min_n,n_lst[i])
    max_n = max(max_n,n_lst[i])
def ezin(start,end):
    global M
    global bestMoney
    if start > end:
        return
    goodMoney = (start+end)//2
    sum_nn = 0
    for money in n_lst:
        if money >= goodMoney:
            sum_nn += goodMoney
        else:
            sum_nn += money
    if M < sum_nn:
        ezin(start,goodMoney-1)
    else:
        bestMoney = goodMoney

        ezin(goodMoney+1,end)
# if min_n == max_n:
#     if min_n*N <= M:
#         print(min_n)
#     else:
#         print(M//N)
# else:
ezin(1,max_n)
    # ezin(min_n,max_n)은 왜 안됨
    # 같을 때나 이래저래 문제가 많다. 그냥 다 돌자
print(bestMoney)
    
        
    