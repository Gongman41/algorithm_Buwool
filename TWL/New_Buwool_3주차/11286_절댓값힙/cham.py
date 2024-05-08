import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
num_arr = []
# 일단 다 양수로 저장해야 절댓값 작은 걸 뽑아낼 수 있음
for _ in range(N):
    x = int(input())
    if x != 0:  # 0이 아닌 경우 -> 배열에 숫자 넣기
        heapq.heappush(num_arr, (abs(x), x))    # 절댓값한 값과 원래 값을 튜플 형태로
    else:   # 0인 경우 -> 절댓값 가장 작은 수 출력한 뒤 제거
        if num_arr:
            print(heapq.heappop(num_arr)[1])
        else:
            print(0)