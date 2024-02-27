import sys
# sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    n = int(input())        # 당근의 개수
    carrot = list(map(int, input().split()))    # 당근의 크기
    cnt = 1
    cnt_lst = []
    i = 0
    while i + 1 < n:
        if carrot[i] < carrot[i+1]:
            cnt += 1
            cnt_lst.append(cnt)
            i += 1
        else:
            cnt = 1
            cnt_lst.append(cnt)
            i += 1
    # print(cnt_lst)
    print(f'#{test} {max(cnt_lst)}')