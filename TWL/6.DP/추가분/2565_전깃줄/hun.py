N = int(input())
lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort()
# print(lst)
new_lst = []
for j in lst:
    new_lst.append(j[1])
# print(new_lst)



def check(new_lst):
    adp = [1] * N
    for a in range(1, N):
        for b in range(a):
            if new_lst[a] > new_lst[b]:
                adp[a] = max(adp[a], adp[b]+1)
    aaa = N - max(adp)
    return aaa


qwe = check(new_lst)
new_lst.sort(reverse=True)
asd = check(new_lst)

print(min(qwe,asd))
# bdp = [1] * N
# for c in range(1, N):
#     for d in range(c):
#         if new_lst[c] < new_lst[d]:
#             bdp[c] = max(bdp[c], bdp[d]+1)
# bbb = N - max(bdp)

# print(aaa, bbb)
# print(min(aaa, bbb))

'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
'''