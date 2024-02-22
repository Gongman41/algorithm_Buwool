import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

wt = t % (2*w)
ht = t % (2*h)

wl = [i for i in range(p, w)] + [i for i in range(w, 0, -1)] + [i for i in range(0, p)]
hl = [i for i in range(q, h)] + [i for i in range(h, 0, -1)] + [i for i in range(0, q)]


print(wl[wt], hl[ht])


