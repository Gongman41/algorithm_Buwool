import sys
sys.stdin = open('input.txt')
'''
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    result = [0] * 8

    while N != 0:
        if N >= 50000:
            N -= 50000
            result[0] += 1
        elif 50000 > N >= 10000:
            N -= 10000
            result[1] += 1
        elif 10000> N >= 5000:
            N -= 5000
            result[2] += 1
        elif 5000 > N >= 1000:
            N -= 1000
            result[3] += 1
        elif 1000 > N >= 500:
            N -= 500
            result[4] += 1
        elif 500 > N >= 100:
            N -= 100
            result[5] += 1
        elif 100 > N >= 50:
            N -= 50
            result[6] += 1
        elif 50 > N >= 10:
            N -= 10
            result[7] += 1
    print(f'#{tc}')
    print(*result)
    '''


T = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T + 1):
    N = int(input())
    result = [0] * 8
    for i in range(8):
        while N >= money[i]:
            N -= money[i]
            result[i] += 1
    print(f'#{tc}')
    print(*result)
