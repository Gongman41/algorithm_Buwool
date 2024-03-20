import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B
result.sort()
print(*result)