import sys
sys.stdin = open('input.txt')
'''
1 2로 10을 만들려면
어차피 2를 1 2개로 만들 수 있다는 경우를 가정
dp = [0,0,0,0,0,0,0,0,0,0,0]
개수로 따졌을때
1.
1 2로 1000
1 2 2 2
'''
T = int(input())
for test_case in range(T):
    N = int(input())
    coins = list(map(int,input().split())) # 각 동전이 주어진다.
    goal  = int(input()) # 해당 금액을 만들면된다.
    dp = [0] * (goal+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin,goal+1):
            dp[i] += dp[i-coin]           

    print(dp[goal])