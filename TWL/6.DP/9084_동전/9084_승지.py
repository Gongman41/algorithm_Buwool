# 테케 개수
T = int(input())

for tc in range(T):
    # 동전 개수
    n = int(input())

    # 동전 금액
    money = list(map(int, input().split()))
    money.insert(0,0)

    # 만들어야 할 금액
    goal = int(input())

    dp = [0] * (goal+1)
    # 0원을 만드는 가지수는 1가지, 돈 안 내면 됨
    dp[0] = 1
    # 모든 경우의 수들을 합해야 함
    for coin in money:
        for i in range(1, goal+1):
            if i-coin < 0:
                continue
            dp[i] += dp[i-coin]

    print(dp[goal])