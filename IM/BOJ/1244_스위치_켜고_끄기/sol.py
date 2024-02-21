import sys
sys.stdin = open('input.txt')

N = int(input())
switch = list(map(int, input().split()))
switch.insert(0, -1)
S = int(input())
# 남자 1, 여자 2
# 성별, 받은 수 (index + 1의 값)
data = list(map(int, input().split()) for _ in range(S))

# 남자 : 받은 수의 배수 번호 상태 변경
# 여자 : 받은 수를 포함하여 받은 수의 좌우가 대칭인 동안 모두 변경
for rule, idx in data:
    origin_idx = idx    # 배수 증가를 위한 원본 유지
    if rule == 1:   # 남자인 경우,
        while idx < len(switch):  # 범위를 벗어나지 않는 동안,
            switch[idx] = int(not switch[idx])  # 반대값의 정수
            idx += origin_idx
    else:           # 여자인 경우
        n = 1   # 좌우 증가할 값
        while 1 <= idx - n and idx + n <= N: # 좌우 범위조절
            if switch[idx-n] == switch[idx+n]:
                switch[idx - n] = int(not switch[idx - n])
                switch[idx + n] = int(not switch[idx + n])
                n += 1
            else:
                break
        switch[idx] = int(not switch[idx])

# 한 줄에 20개 까지 출력
for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if not i % 20:
        print()