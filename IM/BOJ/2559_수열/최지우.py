import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
temp = list(map(int, input().split()))

start = 0
end = K
tmp = 0
for i in range(K):
    tmp += temp[i]

maxi = tmp
while end != N:
    tmp += temp[end]
    tmp -= temp[start]
    maxi = max(maxi, tmp)
    start += 1
    end += 1
print(maxi)