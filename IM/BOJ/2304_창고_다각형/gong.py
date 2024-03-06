import sys
sys.stdin = open('input.txt')
N = int(input())
circle_lt = [list(map(int,input().split())) for _ in range(N)]
circle_lst = sorted(circle_lt,key = lambda x:x[0])
top_cir = 0
top_cir_list = []
for n in range(N):
    if top_cir < circle_lst[n][1]:
        top_cir = circle_lst[n][1]
        top_cir_list.append(circle_lst[n])
f_sum = 0
l_cir = 0
for t in range(len(top_cir_list)-1):
    f_sum += (top_cir_list[t+1][0]-top_cir_list[t][0])*top_cir_list[t][1]

r_sum = 0
r_top_cir = 0
for m in range(N-1,-1,-1):
    if r_top_cir < circle_lst[m][1]:

        r_sum += (circle_lst[m][1]-r_top_cir)*(circle_lst[m][0] - top_cir_list[-1][0])
        r_top_cir = circle_lst[m][1]
    if r_top_cir == top_cir:
        break
print(r_sum+f_sum+top_cir)



