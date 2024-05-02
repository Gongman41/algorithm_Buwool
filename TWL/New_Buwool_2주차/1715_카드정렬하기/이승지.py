import sys
import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

total_cost = 0
while len(cards) > 1:
    # 가장 작은 두 카드 묶음을 꺼내서 합칩니다.
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a + b

# 두 묶음을 합친 비용을 누적하고, 합친 결과를 다시 큐에 넣습니다.
total_cost += sum_value
heapq.heappush(cards, sum_value)
print(total_cost)