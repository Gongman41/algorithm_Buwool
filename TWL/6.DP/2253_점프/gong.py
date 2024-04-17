N,M = map(int,input().split())
n_lst = [1]*(N+1)
for _ in range(M):
    n_lst[int(input())] = 0
i = 1
while not (i*(i+1)/2 >= N-1 and N-1 > i*(i-1)/2):
    i+=1
print(i)



'''
2 1
3 1  4 2
4 1 5 2 5 1 6 2 7 3
'''
# 가는 길 못가는 곳 뺴고. dp에 널뛰기 횟수,널뛰기 거리 저장. 널뛰기 횟수가 작으면 거리도 더 큰가?  널뛰기 횟수 비교해서 적은 놈 거리 저장. 
# 최단거리 갱신..? 
# 크기가 작은 돌은 어떡해