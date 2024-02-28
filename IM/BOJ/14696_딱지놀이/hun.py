import sys
sys.stdin = open('input.txt')

R = int(input())    # 라운드

for _ in range(R):  # 라운드 진행
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    lst_a.pop(0)
    lst_b.pop(0)
    cnt_a = []
    cnt_b = []
    for i in range(1, 5):
        cnt_a.append(lst_a.count(i))
        cnt_b.append(lst_b.count(i))
    # print(cnt_a)
    # print(cnt_b)
    if cnt_a[3] > cnt_b[3]:
        print('A')
    elif cnt_a[3] < cnt_b[3]:
        print('B')
    else:
        if cnt_a[2] > cnt_b[2]:
            print('A')
        elif cnt_a[2] < cnt_b[2]:
            print('B')
        else:
            if cnt_a[1] > cnt_b[1]:
                print('A')
            elif cnt_a[1] < cnt_b[1]:
                print('B')
            else:
                if cnt_a[0] > cnt_b[0]:
                    print('A')
                elif cnt_a[0] < cnt_b[0]:
                    print('B')
                else:
                    print('D')