import sys
N,K = map(int,input().split())
item_lst = [[0,0]]
for _ in range(N):
    W,V = map(int,sys.stdin.readline().split())
    item_lst.append([W,V])
# item_lst.sort(reverse=True)
# dp = [0]*(N+1)
# max_val = 0
# while True:
#     weight = 0
#     tem = 0
#     for j in range(N):
#         for i in range(N):
#             if weight + item_lst[i][1] > K:
#                 continue
#             elif weight + item_lst[i][1] == K:
#                 weight += item_lst[i][1]
#                 break
#             else:
#                 weight += item_lst[i][1]...

d = [[0]*(K+1) for _ in range(N+1)]



for item in item_lst:
    w,v = item
    for i in range(K,w-1,-1):
        d[i] = max(d[i],d[i-w]+v)
print(d[-1])
                
            
    
# 현재 무게, 가치값 합계. dp에 저장
# 무게는 나가지만 가치가 높은 놈, 가볍지만 낮은 놈...
# 가중치가 높은 놈부터. 넣어서 딱 맞으면 끝
    