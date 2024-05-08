import sys
input = sys.stdin.readline


def make_tree(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    mid = (start + end) // 2
    left = make_tree(node*2, start, mid)
    right = make_tree(node*2 + 1, mid + 1, end)

    tree[node] = left+right
    return tree[node]


def find(node, start, end):
    if y < start or end < x:
        return 0

    if x <= start and end <= y:
        return tree[node]

    mid = (start + end) // 2
    left = find(node*2, start, mid)
    right = find(node*2 + 1, mid+1, end)

    return left+right


def change(node, start, end):
    if a < start or end < a:
        return tree[node]

    if start == end == a:
        tree[node] -= nums[a]
        tree[node] += b
        return tree[node]

    mid = (start + end) // 2
    left = change(node*2, start, mid)
    right = change(node*2 + 1, mid+1, end)

    tree[node] = left + right
    return left+right


N, Q = map(int, input().split())
nums = list(map(int, input().split()))
tree = [0] * (4*N)

make_tree(1, 0, N-1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    a -= 1
    if x > y:
        x, y = y, x

    print(find(1, 0, N-1))
    change(1, 0, N-1)
    nums[a] = b
