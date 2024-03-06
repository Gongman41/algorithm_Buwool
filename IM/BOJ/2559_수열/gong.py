# import sys
from collections import deque
# sys.stdin = open('input.txt')
N,K = map(int,input().split())
lst = list(map(int,input().split()))
hot_dq = deque(lst[:K])
max_n = sum(lst[:K])
cur = max_n
for n in range(K,N):
    hot_dq.append(lst[n])
    cur = cur + lst[n]-hot_dq.popleft()
    max_n = max(max_n,cur)
print(max_n)
    
    