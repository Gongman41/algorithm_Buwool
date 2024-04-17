import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:     # 증가한다면
            dp[i] = max(dp[i], dp[j]+1)
        # 여기에서 max로 비교해줘야 하는 이유
        # dp = [1, 2, 3, 4, 3, 2, 5, 6]
        # arr = [10, 15, 20, 30, 20, 15, 40, 50]
print(max(dp))



