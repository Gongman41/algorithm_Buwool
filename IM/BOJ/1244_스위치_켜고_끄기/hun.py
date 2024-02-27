import sys

sys.stdin = open('input.txt')


def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N + 1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N // 2):
            if num + k > N or num - k < 1: break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()

# def men(switch, num):
#     for i in range(1, len(switch) + 1):  # 스위치 번호 i
#         if num * i < len(switch):
#             switch[num * i] += 1
#         else:
#             break
#     return switch
#
#
# def women(switch, num):
#     max_range = range(0, 0)
#     for i in range(1, len(switch) + 1):
#         if num + i <= len(num) and num - i > 0:
#             if switch[num - i] == switch[num + i]:
#                 max_range = range(num - i, num + i + 1)
#             elif switch[num - i] != switch[num + i]:
#                 pass
#         else:
#             break
#     return switch
