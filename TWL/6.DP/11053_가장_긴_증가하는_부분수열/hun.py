'''
수열에서 가장 긴 부분 수열이 나오려면~~??
수열에서 가장 긴 ...
부분 수열
각 각 칸을 이동하면 최댓값을 적어두고 더큰 숫자가 나올때 마다 최댓값을 갱신을 해준다.
이게 되려나
'''
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