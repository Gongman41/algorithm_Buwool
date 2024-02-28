# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    n = int(input())
    carrots = list(map(int, input().split()))

    max_count = 0
    count = 0
    before = 0
    for c in carrots:
        if c <= before:
            # 전에 거 보다 작으면 연속으로 캔 거 일단 업뎃해야징
            if count > max_count:
                max_count = count
            # 누적된 거 0으로 만들어요~
            count = 0
        # 사이즈 신경쓰지 말고 일단 당근 하나 캤으니까
        count += 1
        # 캔 당근이 기준이 되겠지요
        before = c
    # 끝까지 가면 또 업뎃해줘야지용
    if count > max_count:
        max_count = count

    print(f'#{test_case} {max_count}')