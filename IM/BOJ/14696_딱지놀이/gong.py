import sys
sys.stdin = open('input.txt')
N = int(input())
for _ in range(N):
    a,*ast = map(int,input().split())
    b,*bst = map(int,input().split())
    ast.sort(reverse=True)
    bst.sort(reverse=True)
    winner = 'O'
    for i in range(min(len(ast),len(bst))):
        if ast[i] > bst[i]:
            winner = 'A'
            break
        elif ast[i] < bst[i]:
            winner = 'B'
            break
    if winner == 'O':
        if len(ast) > len(bst):
            winner = 'A'
        elif len(ast) < len(bst):
            winner = 'B'
        else:
            winner = 'D'
    print(winner)