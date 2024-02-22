import sys
sys.stdin = open('input.txt')

N = int(input())
sw = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    s, c = map(int, input().split())
    if s == 1:
        for i in range(N):
            x = i+1
            if x%c == 0:
                if sw[i] == 1:
                    sw[i] = 0
                else:
                    sw[i] = 1
    else:
        tmp = 0
        while c-1-tmp >=0 and c-1+tmp < N:
            if sw[c-1 - tmp] == sw[c-1 + tmp]:
                tmp += 1
            else:
                break

        for i in range(c-1 - (tmp-1), c-1 + (tmp)):
            if sw[i] == 1:
                sw[i] = 0
            else:
                sw[i] = 1

while len(sw) >= 20:
    sl = sw[:20]
    print(*sl)
    sw = sw[20:]
print(*sw)