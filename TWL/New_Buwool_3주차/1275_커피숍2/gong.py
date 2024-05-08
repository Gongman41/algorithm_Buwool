import sys
input=sys.stdin.readline

def init(node, start , end):

    if start==end:
        tree[node]=L[start]
        return # 리턴 필수

    init(node * 2, start, (start + end) // 2)
    init(node * 2 + 1, (start + end) // 2 + 1, end)

    tree[node]=tree[node*2]+tree[node*2+1]

def update(node, start , end , index , value):

    if index>end or index<start:
        return

    if index<=start and index>=end: # 포함관계라면
        tree[node]=value
        return

    update(node*2 , start , (start+end)//2 , index  ,value)
    update(node*2+1 , (start+end)//2+1 , end ,index , value)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(node , start , end , left , right):

    if left>end or right<start:
        return 0 # 범위밖이면 0을 반환한다.

    if left<=start and right>=end: #포함관계라면
        return tree[node]


    return query(node*2 , start , (start+end)//2 , left , right) + query(node*2+1 , (start+end)//2+1 , end , left ,right)


N,Q=map(int,input().split())
tree=[0]*(1<<22)
L=list(map(int,input().split()))
init(1 , 0, N-1)
for i in range(Q):

    x,y,a,b=map(int,input().split())

    a-=1 ; x-=1 ; y-=1
    if x>y:
        x,y=y,x

    print( query(1, 0, N-1, x , y))

    update(1 , 0, N-1,a,b)