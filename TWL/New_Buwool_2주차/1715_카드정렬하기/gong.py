# 트리? 30 40 50 60
'''
70 110
180
360
'''
import sys
from heapq import heappop,heappush
sys.stdin.readline
N = int(input())
sum_n = 0
fheap = []

for _ in range(N):
    heappush(fheap,int(input()))
while  True :
    if len(fheap) == 1:
        break
        
    else:
        a = heappop(fheap)
        b = heappop(fheap)
        sum_n += a+b
        heappush(fheap,a+b)
print(sum_n)
        
# 매번 정렬? 힙큐
# if N%2 == 0:
#     for _ in range(N):
#         sum_n += int(input())
# 이것도 살려야.
    # 매 턴 어떤 걸 살리냐. 제일 큰걸 살리는 게 맞나