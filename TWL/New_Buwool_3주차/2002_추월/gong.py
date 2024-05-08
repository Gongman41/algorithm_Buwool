# import sys
# input = sys.stdin.readline
# N = int(input())
# lst = []
# cnt = 0
# fast_cars = set()
# for _ in range(N):
#     lst.append(input())
# cur =0
# for _ in range(N):
#     next = input()
#     if lst[cur] != next:
#         if lst[cur] not in fast_cars:
#             cnt += 1
#             fast_cars.add(next)
#         while cur <=N-1 and lst[cur] != next:
#             cur +=1
        
#     else:
#         cur += 1
# # lst에서 먼저 지나간 애들도 없애줘야됨   
    
# print(cnt)

N = int(input())
# 딕셔너리에 차번호:순서 형태로 저장
in_cars = {}
out_cars = {}

for i in range(N):
    car = input()
    in_cars[car] = i

for i in range(N):
    car = input()
    out_cars[car] = i

count = 0
out_keys = list(out_cars.keys())
# 지금 나온 차의 들어간 순서보다 나중에 나온 차의 들어간 순서가 앞인 경우에는 추월
for i in range(0, len(out_keys)-1):
    now_in = in_cars[out_keys[i]]
    for j in range(i+1, len(out_keys)):
        next_in = in_cars[out_keys[j]]
        if next_in < now_in:
            count += 1
            break

print(count)