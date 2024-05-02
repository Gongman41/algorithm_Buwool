import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heappush(cards, int(input()))

result = 0
while len(cards) > 1:
    a, b = heappop(cards), heappop(cards)
    result += a+b
    x = a + b
    heappush(cards, x)

    # print(cards)

print(result)