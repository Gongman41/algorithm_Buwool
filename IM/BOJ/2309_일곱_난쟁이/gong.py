import sys
sys.stdin = open('input.txt')

lst = []
for _ in range(9):
    lst.append(int(input()))
for i in range(1<<9):
    tem = []
    for j in range(9):
        if i&(1<<j):
            tem.append(lst[j])
    if sum(tem) == 100 and len(tem) == 7:
        lst = tem
        break
lst.sort()
for s in lst:
   print(s)



