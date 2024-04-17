
# num = input()
# num2 = input()
# count = 0
# for i in range(1<<len(num)):
#     tem = []
#     for j in range(len(num)):
#         if i &(1<<j):
#             tem.append(num[j])
#     for n in range(1<<len(num2)):
#         tem2 = []
#         for m in range(len(num2)):
#             if n & (1<<m):
#                 tem2.append(num2[m])
#         if tem == tem2:
#             count = max(count,len(tem))
             
# print(count)        


A = input()
B = input()

m, n = len(A), len(B)
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            # 한발자국 갱신
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # 물타기

print(dp[m][n])

