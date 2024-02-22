import sys
sys.stdin = open('input.txt')

N = int(input())

link = []
opp = [5, 3, 4, 1, 2, 0]
for _ in range(N):
    dice = list(map(int, input().split()))
    l = {i:0 for i in range(1, 7)}
    for j in range(6):
        l[dice[j]] = dice[opp[j]]
    link.append(l)

maxi = 0
for case in range(1, 7):
    nxt = link[0][case]
    tmp = 6 * N
    i = 0
    while i < N:
        nxt = link[i][case]
        if case == 6 or nxt == 6:
            tmp -= 1
            if case == 5 or nxt == 5:
                tmp -= 1
        case = nxt
        i += 1
    maxi = max(maxi, tmp)
print(maxi)




# for i in range(1, 7):
#     start = dices[0][i]
#     for j in range(N-1):




'''
맨밑에꺼 쌓는순간
최대값 계산 가능하게
인덱스로 1-6 2-4 3-5 링크
6 4 5 2 3 1

최대 6 * N해놓고
링크 쭉 따라가면서
6 빠지면 -1
5도 빠지면 -2
'''