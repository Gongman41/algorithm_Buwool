import sys
sys.stdin = open('input.txt')

aword = input()
bword = input()
a = min(len(aword), len(bword))
b = max(len(aword), len(bword))
dp = [[0] * (b + 1) for _ in range(a+1)]
for i in range(1,a+1): # 처음부터 끝까지 돌아봄
    for j in range(1,b+1): # 그 지점부터, 끝까지 돌아봄
        if i == 0 and j == 0:
            continue
        if len(aword) == a:
            if aword[i-1] == bword[j-1]: # 만약 그 단어가 공통 단어이면
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            if aword[j-1] == bword[i-1]: # 만약 그 단어가 공통 단어이면
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)
print(dp[-1][-1])