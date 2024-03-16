K,N = map(int,input().split())
sum_k = 0


k_list = []
for k in range(K):
    k_list.append(int(input()))
    sum_k += k_list[k]
k_list.sort()

# for i in range(sum_k,-1,-1):
    # 최대 높이 i 선정. 이진으로 선정
start = 1
end = sum_k//N

def ezin(i):

    cnt = 0
    for j in range(K-1,-1,-1):

        if k_list[j] // i >= 1:
            cnt += k_list[j] // i
        else:
            break
    return cnt
    


while start != end:
    i = (start+end)//2
    


    
    
    
    
    cnt = ezin(i)
    if cnt < N:
        
        end = i-1
    else:
        if ezin(i+1) < N:
            print(i)
            break
        else:
            start = i + 1
            
    
else:
    
    print((start+end)//2)
