n, k = map(int, input().split())  # n 물건의 개수, k 배낭의 최대 무게


weights = [0] * n
values = [0] * n

for i in range(n):
    w, v = map(int, input().split())
    weights[i] = w
    values[i] = v
# x축 각 배낭의 최대 무게
# y축 물건의 최대 개수
dp = [[0] * (k + 1) for _ in range(n + 1)]

# 각 물건에 대해서 배낭에 넣는다고 생각
for i in range(1, n + 1):  # 물건
    for j in range(1, k + 1):  # 배낭
        if weights[i - 1] > j:  # 현재 물건의 무게가 배낭의 무게보다 크면 해당 물건을 선택몬함
            dp[i][j] = dp[i - 1][j]  # 그럼 그대로 쓴다
        else:  # 현재 물건의 무게가 배낭의 무게보다 작거나 같으면 해당 물건을 선택
            # 해당 물건을 선택하지 않은 경우 vs 선택한 경우 -> 더 큰 가치를 선택
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])


print(dp[n][k])



'''
4 7
6 13
4 8
3 6
5 12
'''




