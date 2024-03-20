N= int(input())
n_list = list(map(int,input().split()))
count_dict = {}
for n in range(N):
    count_dict.setdefault(n_list[n],0)
    count_dict[n_list[n]] += 1
M = int(input())
m_list = list(map(int,input().split()))
for m in m_list:
    print(count_dict.get(m,0),end = ' ')