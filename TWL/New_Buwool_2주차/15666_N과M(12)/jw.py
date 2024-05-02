def nm(idx, cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(idx, n):
        result.append(num[i])
        nm(i, cnt+1)
        result.pop()


N, M = map(int, input().split())
num = list(set(map(int, input().split())))
num.sort()

result = []
n = len(num)
nm(0, 0)


# from itertools import combinations_with_replacement
#
# N, M = map(int, input().split())
# num = list(set(map(int, input().split())))
# num.sort()
#
# for i in combinations_with_replacement(num, M):
#     print(*i)
