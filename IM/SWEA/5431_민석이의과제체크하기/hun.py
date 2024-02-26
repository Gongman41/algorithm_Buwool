import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    student = []
    for i in range(N+1):
        student.append(i)
    # print(student)
    for num in lst:
        student.remove(num)
    student.pop(0)
    print(f'#{tc}', *student)