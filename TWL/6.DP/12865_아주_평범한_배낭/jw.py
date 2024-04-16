N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

dp = [[0] * (K+1) for _ in range(N+1)]

# 총 무게 K 까지 그때 그때의 최대 가중치를 리스트에 저장
# 위 리스트를 2차원으로 N개
# 각 물건의 무게, 가중치
for i in range(1, N+1):
    # 각 배열에는 정확히 j만큼 무게를 채울 수 있는 경우가 있다면
    # 이미 있는 값이랑 새로 넣을 가중치를 비교, 큰 값 저장
    # 그런 경우가 없으면 ?
    # 다른 물건을 넣어서 정확히 무게를 채울 수 있었을 때의 값이 저장됨

    # 무게를 1부터 K까지 N번 순회
    for j in range(K+1):
        w, v = arr[i-1]
        if j < w:
            # 위에서 받아와서 저장 (넣을 수 있었을 때의 최대값)
            dp[i][j] = dp[i-1][j]
        else:
            # 넣을 수 있으면, 넣어보고 큰 값 저장
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[N][K])
# for i in range(N+1):
#     print(dp[i])
