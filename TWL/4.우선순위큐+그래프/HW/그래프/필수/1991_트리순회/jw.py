N = int(input())

tree = [list(map(str, input().split())) for _ in range(N)]

def preorder(i, result, visited):
    result.append(tree[i][0])
    visited.append(i)
    
    if tree[i][1] != '.':
        for x in range(N):
            if tree[i][1] == tree[x][0] and x not in visited:
                preorder(x, result, visited)

    if tree[i][2] != '.':
        for x in range(N):
            if tree[i][2] == tree[x][0] and x not in visited:
                preorder(x, result, visited)

    return result


def inorder(i, result, visited):
    if tree[i][1] != '.':
        for x in range(N):
            if tree[i][1] == tree[x][0] and x not in visited:
                inorder(x, result, visited)

    result.append(tree[i][0])
    visited.append(i)

    if tree[i][2] != '.':
        for x in range(N):
            if tree[i][2] == tree[x][0] and x not in visited:
                inorder(x, result, visited)

    return result

def postorder(i, result ,visited):
    if tree[i][1] != '.':
        for x in range(N):
            if tree[i][1] == tree[x][0] and x not in visited:
                postorder(x, result, visited)

    if tree[i][2] != '.':
        for x in range(N):
            if tree[i][2] == tree[x][0] and x not in visited:
                postorder(x, result, visited)

    result.append(tree[i][0])
    visited.append(i)

    return result

print(''.join(preorder(0, [], [])))
print(''.join(inorder(0, [], [])))
print(''.join(postorder(0, [], [])))