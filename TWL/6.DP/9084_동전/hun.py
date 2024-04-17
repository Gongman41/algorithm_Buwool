def dynamic_puo():
    dp = [0] * (money+1)
    dp[0] = 1
    for coin in lst_coin:
        for k in range(1, money+1):
            if k >= coin:
                dp[k] += dp[k - coin]
    print(dp[money])


T = int(input())
for _ in range(T):
    cnt_coin = int(input())
    lst_coin = list(map(int, input().split()))
    money = int(input())
    dynamic_puo()


    '''
    1원 2원 짜리로
    1000원을 만들어야 한다
    몇개 만들수 있냐
    
    처음부터 시작해서 그다음거에 영향을 어떻게 미치는가
    
    1 5 10 짜리로
    100원을 만들어야 한다
    10원짜리 10개

    '''





