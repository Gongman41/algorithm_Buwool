import sys
sys.stdin = open('input.txt')


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

w, h = w, h

tp = (p + t) // w
tq = (q + t) // h

if tp % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if tq % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)
