import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
card = [int(input()) for _ in range(N)]
heapq.heapify(card)
result = 0
while len(card) > 1:
    min_card = heapq.heappop(card)
    next_card = heapq.heappop(card) + min_card
    heapq.heappush(card, next_card)
    result += next_card
print(result)