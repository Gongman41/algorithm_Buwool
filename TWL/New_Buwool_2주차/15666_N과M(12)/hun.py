import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    heapq.heappush(lst, int(input()))

total_cost = 0
while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    sum_value = a + b

    total_cost += sum_value
    heapq.heappush(lst, sum_value)

print(total_cost)