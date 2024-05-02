import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    command = input().split()
    if len(command) == 1:
        if command[0] == 'empty':
            S = []
        elif command[0] == 'all':
            S = [i for i in range(1, 21)]
    else:
        x = int(command[1])
        if command[0] == 'add':
            if x in S:
                continue
            else:
                S.append(x)
        elif command[0] == 'remove':
            if x in S:
                S.remove(x)
            else:
                continue
        elif command[0] == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif command[0] == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.append(x)
