import sys

input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    c, *n = input().split()

    if n:
        n = int(n[0])

    if c == 'add':
        S |= 1 << n
    elif c == 'remove':
        S &= ~(1 << n)
    elif c == 'check':
        if S & (1 << n):
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        S ^= 1 << n
    elif c == 'all':
        S = (1 << 21) - 1
    elif c == 'empty':
        S = 0
