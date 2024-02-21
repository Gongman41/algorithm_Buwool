import sys
sys.stdin = open('input.txt')


for i in range(4):
    # 모든 선분 정보
    ax, ay, ap, aq, bx, by, bp, bq = map(int, input().split())
    fw = set(range(ax, ap+1))   # 첫번째 네모의 너비 선분
    fh = set(range(ay, aq+1))   # 첫번째 네모의 높이 선분
    sw = set(range(bx, bp+1))   # 두번째 네모의 너비 선분
    sh = set(range(by, bq+1))   # 두번째 네모의 높이 선분
    w = fw & sw     # 너비들 간의 교집합
    h = fh & sh     # 높이들 간의 교집합
    if not all([w, h]):     # 교집합이 하나도 없다면
        print('d')          # 공통 부분 없음
    else:
        # 너비와 높이가 각각 하나씩만 동일하다면 점
        if len(w) == 1 and len(h) == 1:
            print('c')
        # 너비나 높이 둘중 한 곳이 하나만 동일하다면 선분
        elif len(w) == 1 or len(h) == 1:
            print('b')
        # 그 외 직사각형
        else:
            print('a')
