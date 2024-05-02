def dfs(cur,last):
    if cur == M:
        result.add(tuple(tem))
        return
    for i in range(last,N):
        tem.append(n_list[i])
        dfs(cur+1,i)
        tem.pop()
        

N,M = map(int,input().split())
n_list = list(map(int,input().split()))
n_list.sort()
tem = []
result = set()
# for i in range(1<<N):
#     cnt = 0
#     tem = []
#     for j in range(N):
        
#         if i&(1<<j):
#             cnt +=1
#             tem.append(n_list[j])
#     if cnt == M:
#         result.add(tuple(tem))

dfs(0,0)
result = sorted(result)
for lst in result:                    
    print(*lst)
            

