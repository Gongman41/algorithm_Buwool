import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    result = 0
    con = 1
    for c in range(N-1):
        if carrots[c] < carrots[c+1]:
            con += 1
        else:
            result = max(result, con)
            con = 1
    
    result = max(result, con)
    print(f'#{tc} {result}')
