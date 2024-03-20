import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())    # 가지고 있는 숫자 카드 개수
n_list = list(map(int, input().split()))    # 여긴 중복된 숫자 카드가 있음
M = int(input())    # 주어진 숫자카드 개수
m_list = list(map(int, input().split()))

result = []

cnt_dict = {num: 0 for num in m_list}   # 컴프리헨션 함 써봄ㅎ

for key in n_list:      # 내가 갖고 있는 숫자카드 순회하면서
    if key in cnt_dict:       # 혹시 이거 거기도 있니?
        cnt_dict[key] += 1  # 있으면 value값 올려주렴

for i in m_list:
    result.append(cnt_dict[i])

print(*result)

# for key in n_list:
#     if key in m_list:
#         cnt_dict[key] += 1
#  -> 이렇게 하면 시간 초과 뜨는 이유: in 연산자의 시간 복잡도 때문

# - list, tuple
    # Average: O(n)
    # 하나하나 순회하기 때문에 데이터의 크기만큼 시간 복잡도를 가짐
# - set, dictionary
    # Average: O(1), Worst: O(n)
    # 내부적으로 hash를 통해서 자료들을 저장하기 때문에 시간복잡도가 O(1)가 가능하고
    # O(n)의 경우에는 해시가 성능이 떨어졌을(충돌이 많은 경우) 때 발생