'''
1 2 3 4 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 100 2 101 3 102
1 2 3 100 101 102
'''
import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int,input().split()))
dp = [1] * (n + 1)
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if arr[i] > arr[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
print(max(dp))
