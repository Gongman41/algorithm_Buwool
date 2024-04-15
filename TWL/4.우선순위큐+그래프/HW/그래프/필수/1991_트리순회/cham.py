import sys
sys.stdin = open('input.txt')

def preorder(now):
    if now != '.':
        print(now, end='')
        preorder(tree[now][0])  # 왼쪽 자식
        preorder(tree[now][1])  # 오른쪽 자식

def inorder(now):
    if now != '.':
        inorder(tree[now][0])  # 왼쪽 자식
        print(now, end='')
        inorder(tree[now][1])  # 오른쪽 자식

def postorder(now):
    if now != '.':
        postorder(tree[now][0])  # 왼쪽 자식
        postorder(tree[now][1])  # 오른쪽 자식
        print(now, end='')

N = int(input())
tree = {}
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')