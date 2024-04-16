for tc in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    '''
    dp 문젠데
    제일 작은돈부터 큰돈까지 돌기
    i: 기준 돈 + 1부터 target 까지
    i - coin 에 저장된 개수 를 누적해서 더해주기
    
    '''
    dp = [0] * (target+1)

    for coin in coins:
        dp[coin] += 1
        for i in range(coin+1, target+1):
            dp[i] += dp[i-coin]
    print(dp[-1])

