'''
공집합 S에 연산을 수행함
add x : x를 S에 추가한다 => x가 이미 있으면 무시함
remove x : x를 제거 => 없으면 무시
check x : x가 잇으면 1 없으면 -
toggle x : x 가있으면 제거, 없으면 추가
all : s를 {1,2,,,,20} 으로 바꿈
empty : S를 공집합으로 바꿈
'''

import sys
sys.stdin = open('input.txt')

M = int(sys.stdin.readline())
result = 0
for _ in range(M):
    user_input = sys.stdin.readline().rstrip()
    if user_input == 'all':
        result = (1 << 21) - 1
    elif user_input == 'empty':
        result = 0
    else:
        comment, num = user_input.split()
        num = int(num)
        if comment == 'add':
            # 집합에 원소를 추가
            result |= (1 << num)
        elif comment ==  'remove':
            # 집합에 원소를 제거
            result &= ~(1 << num) 
        elif comment == 'check':
            if result & (1 << num):
                print(1)
            else:
                print(0)
        elif comment == 'toggle':
            result ^= (1 << num)