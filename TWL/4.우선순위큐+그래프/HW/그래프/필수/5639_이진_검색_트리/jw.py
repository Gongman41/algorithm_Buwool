import sys
sys.setrecursionlimit(10**6)

def postorder(t):
    global result
    if not t:
        return
    
    root = t[0]
    if len(t) == 1:
        result.append(root)
        return
    
    left, right = [], []
    for i in t:
        if i == root:
            continue
        if i < root:
            left.append(i)
        else:
            right.append(i)
    postorder(left)
    postorder(right)

    result.append(root)
    return

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

result = []
if tree:
    postorder(tree)
    for i in range(len(result)):
        print(result[i])
