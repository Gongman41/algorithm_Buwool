import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())

# 각 학년별, 여학생, 남학생이 한 방에 사용가능한 인원 수
arr = [[K, K] for _ in range(7)]
cnt = 0

for i in range(N):
    # 성별, 학년
    S, Y = map(int, input().split())
    # 해당 학년의 특정 성별이 더 이상 방에 못들어가면
    if arr[Y][S] == 0:
        arr[Y][S] = K   # 새 방 공급
    if arr[Y][S] == K:  # 새 방에 인원을 넣을거라면
        cnt += 1        # 방 하나 더 추가
    arr[Y][S] -= 1      # 해당 방에 넣을 수 있는 사람 수 감소
print(cnt)

