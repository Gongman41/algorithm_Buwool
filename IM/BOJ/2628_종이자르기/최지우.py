import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
C = int(input())
g_p = [0]
s_p = [0]
for _ in range(C):
    d, p = map(int, input().split())
    if d == 0:
        g_p.append(p)
    else: s_p.append(p)

g_p.sort()
g_p.append(M)
s_p.sort()
s_p.append(N)

mx_g = mx_s = 0
for i in range(1, len(g_p)):
    mx_g = max(mx_g, g_p[i] - g_p[i-1])
for i in range(1, len(s_p)):
    mx_s = max(mx_s, s_p[i] - s_p[i-1])

if mx_g == 0:
    mx_g = M
if mx_s == 0:
    mx_s = N
print(mx_g*mx_s)