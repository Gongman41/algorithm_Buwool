import sys
sys.stdin = open('input.txt')

N = int(input())

idx = 1
for i in range(1, N+1):
    if N == 1:
        print('*')
        break

    if i == 1:
        print('* ' * (i - 1) + '*' * ((N * 4) - (i * 4 - 1)))
    elif i < 3:
        print('* ' * (i - 1) + '*' * ((N * 4) - (i * 4 - 3)))
    else:
        print('* ' * (i - 1) + '*' * ((N * 4) - (i * 4 - 3)) + ' *' * idx)
        idx += 1

    if i == 1:
        print('*')
    elif i == N:
        print('*' + ' *' * (N * 2 - 2))
    else:
        print('* ' * i + ' ' * ((N - i) * 4 - 1) + ' *' * (i - 1))

if N != 1:
    print('*' + ' *' * (N * 2 - 2))

for i in range(N-1, 0, -1):
    print('* ' * i + ' ' * ((N-i) * 4 - 3) + ' *' * i)
    print('* ' * (i - 1) + '*' * ((N - i) * 4 + 1) + ' *' * (i - 1))