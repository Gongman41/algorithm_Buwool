N = int(input())
dp = [0]*(N+2)
dp[2] = 3
if N%2 == 1:
    print(0)
elif N == 2:
    print(3)
else: 
    for i in range(4, N, 2):
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2])*2  + 2
    print(dp[N])