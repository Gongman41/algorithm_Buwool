import heapq, sys

n = int(input())
heap = []

for _ in range(n):
    # 시간 초과 나서 입력속도를 높이기 위함
    value = int(sys.stdin.readline().rstrip())
    if value == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(value), value))