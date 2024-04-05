N = int(input())
sc = list(map(int, input().split()))
M = int(input())
fc = list(map(int, input().split()))

sc.sort()

for c in fc:
    s = 0
    e = N-1
    if sc[s] <= c <= sc[e]:
        while s <= e:
            m = (s+e)//2
            if sc[m] > c:
                e = m-1
            elif sc[m] < c:
                s = m+1
            else:
                print(1, end=' ')
                break
        if sc[m] != c:
            print(0, end=' ')
    else:
        print(0, end=' ')

# dic = {}
# for c in sc:
#     dic[c] = 1

# for c in fc:
#     if c in dic:
#         print(dic[c], end=' ')
#     else:
#         print(0, end=' ')