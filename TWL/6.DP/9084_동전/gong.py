T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n_lst = list(map(int,input().split()))
    M = int(input())
    # count = 0
    # for i in range(1<<N):
    #     tem = 0
    #     for j in range(N):
    #         if i &(1<<j):
    #             tem += n_lst[j]
    #     if tem == M:
    #         count += 1
    # print(count)
    dp = [0]*(M+1)
    dp[0] = 1 # 0원으로 만드는 가지 수 1개
    for coin in n_lst:
        for money in range(M+1):
            if money >= coin: # 금액이 동전의 가치보다 크면
                dp[money] += dp[money-coin] # 해당 dp는 금액 - 동전에 해당하는 dp합
    print(dp[M])
    # 이거 테이블 만드는 법 익숙해져야됨

