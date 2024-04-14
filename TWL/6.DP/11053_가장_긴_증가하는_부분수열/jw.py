A = int(input())
num = list(map(int, input().split()))

dp = [1] * (A)

for i in range(1, A):
    for j in range(i-1, -1, -1):
        if num[i] > num[j]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp))