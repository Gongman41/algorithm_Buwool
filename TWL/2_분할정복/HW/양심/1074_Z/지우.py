import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

n = 2**N

ans = 0

while n != 1:
    
    if r < n//2 and c < n//2: n = n//2

    elif r < n//2 and c >= n//2:
        ans += (n//2)**2; n = n//2
        c -= n
    
    elif r >= n//2 and c < n//2:
        ans += ((n//2)**2)*2; n = n//2
        r -= n

    else:
        ans += ((n//2)**2)*3; n = n//2
        r -= n; c -= n

print(ans)