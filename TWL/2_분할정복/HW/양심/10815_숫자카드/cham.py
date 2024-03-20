import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def binary_search(arr, target, cnt_idx):
    global cnt_list
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:  # 찾았으면
            cnt_list[cnt_idx] += 1
            return
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return

# 중복된 숫자 카드는 없음!
N = int(input())    # 가지고 있는 숫자 카드 개수
n_list = list(map(int, input().split()))
n_list.sort()
M = int(input())    # 주어진 숫자카드 개수
m_list = list(map(int, input().split()))
cnt_list = [0] * M

for i in range(len(m_list)):
    binary_search(n_list, m_list[i], i)

print(*cnt_list)