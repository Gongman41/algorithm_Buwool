import sys
sys.stdin = open('input.txt')


N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    A_info = [0] * 5                # 인덱스 별로, 문양 정보 표기
    for i in range(1, A[0]+1):      # 모든 문양 정보 표기
        A_info[A[i]] += 1
    B = list(map(int, input().split()))     # B도 A와 동일
    B_info = [0] * 5
    for i in range(1, B[0] + 1):
        B_info[B[i]] += 1

    # 모든 경우를 통과 못하면 무승부
    result = 'D'
    # 4, 3, 2, 1 순으로 비교
    for i in range(4, 0, -1):
        if A_info[i] != B_info[i]:      # 동일한 문양에 대해 비교수
            if A_info[i] > B_info[i]:   # 각 조건에 따라
                result = 'A'            # 승자 결정
                break                   # 승자가 나오면 다음 조사 필요 없음. 조사 종료
            elif A_info[i] < B_info[i]:
                result = 'B'
                break
    print(result)