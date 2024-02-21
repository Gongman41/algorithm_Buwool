import sys
sys.stdin = open('input.txt')

# 0번이 바닥이면 5번이 상단
G = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
# 현재 진행중인 주사위 번호, 바닥에 둘 주사위 눈, 누적 합
def search(K, bottom, cnt):
    global result
    # 모든 주사위를 조사할 때까지
    while K != N:
        # 현재 바닥에 둔 주사위 눈이 몇번째 인덱스인지 조사
        for i in range(6):
            if bottom == arr[K][i]:
                bottom_idx = i              # 바닥에 둔 주사위 인덱스를 찾고
                top_idx = G[bottom_idx]     # 반대쪽 주사위 인덱스를 찾은 다음
                top = arr[K][top_idx]       # 상단에 둘 주사위 눈 값을 구한다.
                break

        tmp = list(arr[K])      # 원본 배열을 복사하고
        tmp[top_idx] = 0        # 복사본에 바닥에 둔 눈을 지우고
        tmp[bottom_idx] = 0     # 상단에 둔 눈도 지운다음
        # 다음 주사위의 바닥이 현재 주사위의 상단과 같아야 하므로
        cnt += max(tmp)         # 바닥과 상단을 제외한 가장 높은 수를 구해서 누적하고
        bottom = top            # 다음 조사를 위해 상단을 바닥으로 바꾸고
        K += 1                  # 다음 조사 시작
    result = max(result, cnt)   # 누적값을 최댓값과 비교교

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
# 첫번쨰 주사위는 순서대로 집어넣기
for i in range(6):
    search(0, arr[0][i], 0)

print(result)




