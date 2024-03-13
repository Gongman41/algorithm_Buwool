import sys
sys.stdin = open('input.txt')

# x: 게임 횟수, y: 이긴 게임
x, y = map(int, input().split())
z = y*100 // x
start = 1
end = x
result = x
if z >= 99:     # 승률이 99퍼 이상이면 더 이상 바뀔 수 없음
    print(-1)
else:
    while start <= end:
       mid = (start + end) // 2
       if (y+mid)*100 // (x+mid) > z:
           result = mid
           end = mid - 1
       else:
           start = mid + 1

    print(result)