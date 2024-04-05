N,M = map(int,input().split())
#처음 구간의 값과 다음 구간의 값이 같은 경우. 그 값들 중 가장 작은 값
n_lst = list(map(int,input().split()))
if N == M:
    print(max(n_lst))
else:
    start = max(n_lst)
    end = sum(n_lst)
    max_n = 10e10
    while start <= end:
        middle = (start+end)//2
        tem_m = 0
        cnt = 1
        for i in range(N):
            tem_m += n_lst[i]
            if tem_m > middle:
                tem_m = n_lst[i]
                cnt += 1
        if cnt <= M:
            max_n = min(max_n,middle)
            end = middle -1
        else:
            start = middle +1
    # se_lst = [start,end]


    # for j in range(2):
    #     middle = se_lst[j]
    #     tem_m = 0
    #     cnt = 1
    #     for i in range(N):
    #         tem_m += n_lst[i]
            
    #         if tem_m > middle:
    #             tem_m = n_lst[i]
    #             cnt += 1
        
    #     if cnt <= M:
    #         max_n = min(max_n,middle)
        
        
    
    print(max_n)
        



# def summ(lst,start,end):
#     sum_n = 0
#     for i in range(start,end+1):
#         sum_n += lst[i]
#     return sum_n

# # 최소를 구하는것. 초반 구간을 구하는 것. 구간합의 최대값이 가장 작은 경우
# cnt = 0
# start = 0
# end = N-M
# while start <= end:
#     tem_m = 0
#     middle = (start+end)//2
#     for i in range(middle+1):
#         tem_m += n_lst[i] # 재귀로 해야되는데 리커젼에러 나올듯
#     while 
#     #bfs 초기값 설정하고 나머지 stack으로 싹 계산. 최대값 뽑고 갱신
#     #다음 초기값이 더 작으면 계속 반복
#     # M 자리 수의 수열. 합은 N. 



# 이진 재귀. 이진으로 초기 값 설정. 그다음부터는 남은 M값만큼 여유 남기고 재귀

# 부분집합 만들고 최대 합 구하고 갱신. 그 최대합보다 크면 백트래킹
#     #M은 어떡해. 약간 러시아 국기.
#     while start <= end:
#         middle = (start+end)//2
#         tem_sum = 0
#         tem_md = middle
#         cnt = 0
#         while tem_sum < sum_b:
#             tem_sum += n_lst[tem_md]
#             tem_md += 1
#         if tem_sum == sum_b:
#             start,end = middle,tem_md
#             cnt+=1
#             if cnt == M:
                
#                 break
#         if cnt == M and tem_md:
#             print(sum_b)
#             break
            
                
        
#초반 구간으로 블루레이 크기 구하고 그거가 되는 구간을 이진으로 갈기기

            
#초반구간으로 초기값 구하고 그 다음부터 자를 부분 이진으로. 부분집합으로? 