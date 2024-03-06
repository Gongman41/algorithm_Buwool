# import sys
# sys.stdin = open('input.txt')
W,H = map(int,input().split())
cut_N = int(input())

r_cut = []
c_cut = []
for _ in range(cut_N):
    a,b = map(int,input().split())
    if a == 0:
        r_cut.append(b)
    else:
        c_cut.append(b)
if r_cut and c_cut:
    r_cut.sort()
    c_cut.sort()
    max_r = r_cut[0]
    max_c = c_cut[0]
    for c in range(len(r_cut)-1):
        max_r = max(max_r,r_cut[c+1]-r_cut[c])
    for cc in range(len(c_cut)-1):
        max_c = max(max_c,c_cut[cc+1]-c_cut[cc])
    max_r = max(max_r,H-r_cut[-1])
    max_c = max(max_c,W-c_cut[-1])
    print(max_r * max_c)
elif r_cut and not c_cut:
    r_cut.sort()
    max_r = r_cut[0]
    for c in range(len(r_cut)-1):
        max_r = max(max_r,r_cut[c+1]-r_cut[c])
    max_r = max(max_r,H-r_cut[-1])
    print(max_r * W)
elif c_cut and not r_cut:
    c_cut.sort()
    max_c = c_cut[0]
    for c in range(len(c_cut)-1):
        max_c = max(max_c,c_cut[c+1]-c_cut[c])
    max_c = max(max_c,W-c_cut[-1])
    print(max_c * H)
else:
    print(W*H)
    
    
    
        