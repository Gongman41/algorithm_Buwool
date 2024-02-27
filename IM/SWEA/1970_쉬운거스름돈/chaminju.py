import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    won = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8
    for i in range(8):
        if won >= money[i]:
            cnt[i] = won // money[i]
            won %= money[i]
            if won == 0:
                break
    print(f'#{test}')
    print(*cnt)
