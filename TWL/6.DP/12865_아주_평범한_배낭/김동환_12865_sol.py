import sys
sys.stdin = open('input.txt')
n, k = map(int,input().split())
container = [list(map(int,input().split())) for _ in range(n)]
bags = [0] * (k+1)
for w, v in container:
    for ww in range(k, w-1, -1):
        bags[ww] = max(bags[ww], bags[ww-w] + v)
print(bags[k])