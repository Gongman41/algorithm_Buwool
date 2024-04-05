# import sys
# sys.stdin = open('input.txt')
# nodes = {}
# nodes[1] = [int(input()),0,0,0]
# cur = 1
# while True:
#     try:
#         a = int(input())
#         if a <= nodes[cur][0]:

#             nodes[cur*2] = [a,cur,0,0]
#             nodes[cur][2] = 2*cur

#             cur *= 2
#         else:
#             while cur != 1:
#                 if nodes[cur//2][0] > a:

#                     nodes[2*cur+1] = [a,cur,0,0]
#                     nodes[cur][3] = 2*cur+1
#                     cur = cur * 2 + 1
#                     break
#                 else:
#                     cur //= 2
#             else:
#                 cur =3
#                 nodes[cur] = [a,1,0,0]
#                 nodes[1][3] = 3
#     except EOFError:
#         break
# print(nodes)
# def last(start):
#     if nodes.get(start,0) == 0:
#         return

#     last(start*2)
#     last(start*2+1)
#     print(nodes[start][0])

# last(1)

# #         왼쪽 자식인 경우, 오른쪽 자식인 경우
# #  형제인 경우
# # 조상의 형제인 경우
# # 입력머ㅏㅁ추기

import sys
sys.setrecursionlimit(10**9)

preorder_arr = []

# 엔터 들어올 때까지 입력
while True:
    try:
        preorder_arr.append(int(sys.stdin.readline().rstrip()))
    except:
        break

def postorder(root_idx, end_idx):
    if root_idx > end_idx:
        return
    
    global preorder_arr
    
    # 만약 root보다 큰 값 없는 경우 전부 왼쪽 서브트리로 취급
    right_start = end_idx + 1

    for i in range(root_idx + 1, end_idx + 1):
        if preorder_arr[root_idx] < preorder_arr[i]:
            right_start = i
            break
    
    # root 다음부터 왼쪽 서브트리 탐색
    postorder(root_idx + 1, right_start - 1)

    # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
    postorder(right_start, end_idx)

    # 왼쪽, 오른쪽 서브트리 탐색 끝나면 root 출력
    print(preorder_arr[root_idx])


postorder(0, len(preorder_arr) - 1)