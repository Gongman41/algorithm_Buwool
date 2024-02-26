import sys

sys.stdin = open('input.txt')

N = int(input())

for num in range(1, N + 1):
    cnt = 0
    for i in str(num):
        if i == '3' or i == '6' or i == '9':
            cnt += 1

    if cnt == 0:
        print(num, end=' ')
    else:
        print('-' * cnt, end=' ')
