N = int(input())
# 한 점 기준으로 잡고 한 쪽 면과 높이를 구해야한다.
sum_n = 0

n_lst = [list(map(int,input().split())) for _ in range(N)] 
n_lst.sort()
umgijoon = n_lst[0]
for i in range(1,N-1):
    sum_n += 0.5*abs(umgijoon[0]*(n_lst[i][1]-n_lst[i+1][1]) + n_lst[i][0]*(n_lst[i+1][1]-umgijoon[1])+n_lst[i+1][0]*(umgijoon[1]-n_lst[i][1]))
print(round(sum_n,1))
# 점이 순서대로 안들어와있을수도 ㄷ