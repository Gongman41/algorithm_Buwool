import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())    # 5 3
    A = list(map(int, input().split()))    # 크기는 N
    B = list(map(int, input().split()))     # 크기는 M
    A.sort()
    B.sort()
    result = 0
    start = 0
    for a in range(N):
        while start < M: # start = 1
            if A[a] > B[start]:
                start += 1      # B의 다음 요소로 넘어가서 비교하기 위해
            else:
                result += start
                break
        else:   # while문을 안 돌았다는 건 그 수가 B의 젤 큰 수보다 크다는 거니까
            result += M     # 바로 B의 개수를 더해줌
    print(result)