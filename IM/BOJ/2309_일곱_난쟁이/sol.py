import sys
sys.stdin = open('input.txt')

from itertools import combinations


data = [int(input()) for x in range(9)]

# 전체 요소중, 7개로 만들 수 있는 조합 구성, 그 중 전체 합이 100인경우
result = [x for x in combinations(data, 7) if sum(x) == 100]
# 아무거나 뽑으면 되므로, 0번째 요소를 정렬한다음 출력
for num in sorted(result[0]):
    print(num)
