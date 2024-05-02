import sys
sys.stdin = open('input.txt')

def backtracking(result):
    if len(result) == M:    # 길이가 M과 같아지면 출력 후 return
        print(*result)
        return
    for i in num_lst:   # num_list 순회하면서
        if not result or i >= result[-1]:   # result에 아무것도 없거나 / result 맨 뒤의 값이 i보다 작거나 같다면
            result.append(i)    # 해당 값 append
            backtracking(result)
            result.pop()  # 백트래킹

N, M = map(int, input().split())
num_lst = sorted(set(map(int, input().split())))  # 중복 제거와 정렬을 한번에 처리

result = []
backtracking(result)