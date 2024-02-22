import sys
sys.stdin = open('input.txt')

N = int(input())
h = []
start = 1000
end = 0
for _ in range(N):
    col = list(map(int, input().split()))
    h.append(col)
    start = min(start, col[0])
    end = max(end, col[0]+1)
h.sort(key = lambda x:-x[1])
maxi_h = h[0][1]
l_h = r_h = maxi_h

cur = h[0][0]
left = right = cur

ans = h[0][1] * (end-start)

end -= 1
diff = 0
for i in range(1, N):
    tmp_p = h[i][0]
    tmp_h = h[i][1]
    if tmp_p > right:
        diff += (r_h - tmp_h) * (end - right)
        right = tmp_p
        r_h = tmp_h
    elif tmp_p < left:
        diff += (l_h - tmp_h) * (left - start)
        left = tmp_p
        l_h = tmp_h

ans -= diff
print(ans)