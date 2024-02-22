import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    a, *A = map(int, input().split())
    a, *B = map(int, input().split())
    for c in range(4, 0, -1):
        a = b = 0
        for i in A:
            if i == c:
                a += 1

        for i in B:
            if i == c:
                b += 1

        if a == b:
            continue

        elif a > b:
            result = 'A'
            break
        else:
            result = 'B'
            break
    else:
        result = 'D'
    print(result)
