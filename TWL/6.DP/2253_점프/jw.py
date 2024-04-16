N, M = map(int, input().split())

small = {int(input()) for _ in range(M)}

k = int((2*N)**0.5)
dp = [[10001]*(k+1) for _ in range(N+1)]
dp[2][1] = 1


if 2 in small:
    print(-1)
else:
    for i in range(3, N+1):
        if i in small:
            continue

        for j in range(1, k+1):
            dp[i][j] = min(dp[i-j][j-1:j+2])+1

    print(min(dp[-1]))




'''
더 짧은 횟수로 도착 했어도, N에 딱 맞게 못 뛰는 경우가 있음
8 2
3
6
5번 뛰어서 도착 할 수 있는데, 7에 3번만에 뛰어 간 경우 3, 3으로 와서 8을 못간다
2 (1, 1) > 4 (2, 2) > 7 (3, 3)
7에 4번 뛰어서 4, 2 가 되면 8 갈 수 있음
2 (1, 1) > 4 (2, 2) > 5 (3, 1) > 7 (4, 2) > 8 (5, 1) 
이걸 어떻게 봐
2차원 배열 dp[i][j] 가 의미하는게
i번째 돌로 j 속도만큼 뛰어서 왔을 때의 최소횟수 ? 저장하면 될듯
'''