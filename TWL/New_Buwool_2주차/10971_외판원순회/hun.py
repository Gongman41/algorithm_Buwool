import sys

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N)]

def tsp(start, visited):
    if visited == (1 << N) - 1:
        return costs[start][0] if costs[start][0] > 0 else float('inf')
    
    if dp[start][visited] != 0:
        return dp[start][visited]
    
    min_cost = float('inf')
    
    for next_city in range(N):
        if visited & (1 << next_city) == 0 and costs[start][next_city] > 0:
            cost = costs[start][next_city] + tsp(next_city, visited | (1 << next_city))
            min_cost = min(min_cost, cost)
    
    dp[start][visited] = min_cost
    return min_cost

print(tsp(0, 1))