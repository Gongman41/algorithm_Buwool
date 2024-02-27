import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())                # N: 수강생 수, K: 과제 제출한 사람 수
    student_lst = list(map(int, input().split()))   # 과제 제출한 학생 번호 리스트
    not_submit = []         # 제출 안 한 학생 번호 저장할 리스트
    for i in range(1, N+1):
        if i not in student_lst:
            not_submit.append(i)

    print(f'#{test}', *not_submit)