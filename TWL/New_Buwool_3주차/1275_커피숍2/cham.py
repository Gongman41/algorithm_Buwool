import sys
sys.stdin = open('input.txt')

N, Q = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(Q):
    x, y, a, b = map(int, input().split())
    # 모르겠음..