import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for goal in range(1, money + 1):
            if goal >= coin:   # 목표금액이 coin 보다 작으면 어차피 0 이니까
                dp[goal] += dp[goal-coin]

    print(dp[money])