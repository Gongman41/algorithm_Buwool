N = int(input())
tem = list(map(int,input().split()))
curry = [1]*N

for i in range(1, N):
    for j in range(i):
        if tem[i] > tem[j]:
            curry[i] = max(curry[i], curry[j] + 1)
            # 지금 있는 곳까지 크기비교 갱신

print(max(curry))
# cur = tem[0]
# count = 1
# for i in range(N):
#     if cur < tem[i]:
#         count += 1
#         cur = tem[i]
# print(count)
#  이 순서 그대로. 같거나 작은 놈들 치우고

# 시작점 ...
