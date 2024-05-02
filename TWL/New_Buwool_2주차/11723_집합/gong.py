import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    temp = input().split()
    if temp[0] == 'all' or temp[0] == 'empty':
        query = temp[0]
    else:
        query,n = temp
        n = int(n)
    
    if query == 'add':
        S.add(n)
    elif query == 'remove':
        S.discard(n)
    elif query == 'check':
        if n in S:
            print(1)
        else:
            print(0)
        
    elif query == 'toggle':
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif query == 'all':
        S = set(range(1,21))
    else:
        S = set()
        