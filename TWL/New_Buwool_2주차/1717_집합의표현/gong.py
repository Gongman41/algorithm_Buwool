# def where_is(cur):
#     while type(set_lst[cur]) != set:
#         cur = set_lst[cur]
#     return cur

# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# set_lst = [{i} for i in range(n+1)]
# for _ in range(m):
#     check,a,b = map(int,input().split())
#     if not check:
#         a= where_is(a)
#         b = where_is(b)
#         if a != b:
#             set_lst[a] = set_lst[a]|set_lst[b]
#             set_lst[b] = a
        
#     else:
#         if where_is(a) == where_is(b):
#             print('yes')
#         else:
#             print('no')
        
        # 메모리 초과

import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합

# 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 합집합 연산(두 집합을 합치기 위한 함수)
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 값이 더 작은 쪽을 부모로
        parent[b] = a
    else:
        parent[a] = b
        
for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
    
    