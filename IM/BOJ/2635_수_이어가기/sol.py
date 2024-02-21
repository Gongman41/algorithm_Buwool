import sys
sys.stdin = open('input.txt')


N = int(input())
result = 0
r_arr = []
for i in range(N+1):    # N과 작거나 같은 모든 양의 정수 조사
    arr = [N, i]    # 계산하여 집어 넣을 임시 배열
    tmp = N         # 원본을 유지 하기 위한 임시 변수
    idx = 1         # 계산 대상 idx
    while tmp >= 0:     # 음수가 되면 종료
        # 직전 대상과 현재 대상의 차를 계산
        tmp = arr[idx-1] - arr[idx]
        if tmp >= 0:    # 양수만 다음 값으로 추가
            arr.append(tmp)
        idx += 1

    len_arr = len(arr)
    if len_arr > result:    # 이전 조사 최대길이보다 현재 조사 최대 길이가 더 길면
        result = len_arr    # 바꿔주고
        r_arr = arr         # 배열도 바꿈
print(result)
print(*r_arr)   # 언패킹