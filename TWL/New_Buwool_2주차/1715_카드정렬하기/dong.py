import sys
sys.stdin = open('input.txt')
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for _ in range(N):
    c = int(input())
    pq.put(c)

data1 = 0
data2 = 0
sumi = 0

while pq.qsize()>1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1+data2
    sumi += temp
    pq.put(temp)
    
print(sumi)    