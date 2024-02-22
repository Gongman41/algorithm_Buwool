import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
S = int(input())

shops = []
opp = [(1, 2), (2, 1), (3, 4), (4, 3)]
for _ in range(S):
    shops.append(list(map(int, input().split())))
D = list(map(int, input().split()))

ans = 0
for i in shops:
    if i[0] == D[0]:
        tmp = abs(i[1] - D[1])
    elif (i[0], D[0]) in opp:
        if (D[0]+1)//2 == 1:
            tmp = min((D[1] + i[1]), (N-D[1] + (N-i[1]))) + M
        else:
            tmp = min((D[1] + i[1]), (M-D[1] + (M-i[1]))) + N
    else:
        if D[0] == 1:
            tmp = i[1]
            if i[0] == 3:
                tmp += D[1]
            else: tmp += (N - D[1])
        elif D[0] == 2:
            tmp = (M - i[1])
            if i[0] == 3:
                tmp += D[1]
            else: tmp += (N - D[1])
        elif D[0] == 3:
            tmp = i[1]
            if i[0] == 1:
                tmp += D[1]
            else: tmp += (N - D[1])
        elif D[0] == 4:
            tmp = (N - i[1])
            if i[0] == 1:
                tmp += D[1]
            else: tmp += (N - D[1])
    ans += tmp
print(ans)

