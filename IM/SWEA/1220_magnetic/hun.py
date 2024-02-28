import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(100)]
    cnt = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if lst[j][i] == 1 and len(stack) % 2 == 0:
                stack.append(1)
            elif lst[j][i] == 2 and len(stack) % 2 == 1:
                stack.append(2)
        cnt += len(stack)//2
    print(f'#{tc} {cnt}')






