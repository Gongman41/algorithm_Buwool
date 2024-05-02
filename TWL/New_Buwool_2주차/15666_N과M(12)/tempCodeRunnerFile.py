N,M = map(int,input().split())
n_list = list(map(int,input().split()))
n_list.sort()
result = set()
for i in range(1<<N):
    cnt = 0
    tem = []
    for j in range(N):
        
        if i&(1<<j):
            cnt +=1
            tem.append(n_list[j])
    if cnt == M:
        result.add(tuple(tem))
result = sorted(result)
for lst in result:
    print(*lst)
                    
            

