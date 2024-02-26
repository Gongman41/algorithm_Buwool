import sys
sys.stdin = open('input.txt')

N = int(input())
for num in range(1, N+1):
    in_369 = 1
    num = str(num)
    for i in num:
        if i in '369':
            print('-', end='')
            in_369 *= 0
        else:
            continue
    else:
        if in_369 == 1:
            print(num, end='')
    print(' ', end='')