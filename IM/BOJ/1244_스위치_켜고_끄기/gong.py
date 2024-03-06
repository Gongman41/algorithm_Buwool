import sys
sys.stdin = open('input.txt')
N = int(input())
switch = [0]
switch = switch + list(map(int,input().split()))
M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    if a == 1:
        i = 1
        while b*i <= N:
            switch[b*i] = int(not switch[b*i])
            i += 1
    if a == 2:
        switch[b] = int(not switch[b])
        i = 1
        while 1<= b-i and b+i <= N and switch[b-i] == switch[b+i]:
            switch[b-i] = int(not switch[b-i])
            switch[b + i] = int(not switch[b+i])
            i += 1
j = 1
while 20*j <= N:
    print(*switch[20*(j-1)+1:20*j+1])
    j += 1
print(*switch[20*(j-1)+1:])
