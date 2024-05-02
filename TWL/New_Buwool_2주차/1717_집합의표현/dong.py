import sys
sys.stdin = open('input.txt')

'''
0 a b 는 합집합의 입력
1 a b 는 두 원소가 같은 집합에 있는지 확인함
총 n + 1개의 집합이 있는데, (최대 1000001) 집합에 뭐가 있는지, 그 집합을 합치는지 확인
union - find 사용
부모 노드에서 타고 들어가서, 만약 같아진다면 돌려주고, 아니면 부모노드를 돌려버림
'''
import sys
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b: # 같으면 볼 필요가 없음
        return
    if a != b: # 다르다면
        parent[a] = b # 그냥 a에 b를 넣어주자.

n, m = map(int,sys.stdin.readline().split()) ## n+1 집합의 개수, m은 연산의 개수
parent = [i for i in range(n+1)]
for _ in range(m): # m 번의 입력을 받는다.
    category, a, b = map(int,sys.stdin.readline().split())
    if category == 0: # 만약 a, b를 합쳐야하는 연산이면
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')