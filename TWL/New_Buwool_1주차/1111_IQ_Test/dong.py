import sys
sys.stdin = open('input.txt')

'''
다음 수를 구해줘
그런데 다음에 올 수 있는 수가 여러개면 A
없으면 B를 출력하자
그럼 이전수와 다음수를 비교하여 나올 수 있는 모든 공식을 나타내주면 되나?
1 4 13 40 을 보앗을때
4는 (1*4 + 0), (1*3 + 1), (1*2 + 2), (1 * 1 + 3), (1 * 0 + 4) 이정도
그럼 그 다음 저 공식 내에서 4에서 13이 나올 수 있는 건
*3+1 밖에 없다
그럼 이것만 남겨두고
40까지 적용이 되어버렸다
그럼 다음 정답은 121
1 2 3 4 5 에서도
1 에서 2를 만드는 건 *2+0 *1+1 *0+2 이다 
2에서 3을 만드는건 *1+1 밖에 없고 이게 5까지 유지되어 6
이런식으로 만들어서
들어갈 수 있는 공식의 수를 점점 줄여간다.
1. 만약 중간에 순열이 끊기는 경우,( 리스트가 비어버림 ) => B
2. 만약 마지막까지 갔는데, 적용된 공식의 숫자가 여러개인 경우 => A
3. 하나의 정답이 나오는 경우, 그 숫자를 출력한다.
음수가 나오는 경우와 안나오는 경우로 분기?

'''

from collections import deque

N = int(input()) # 몇개의 수인지
arr = deque(map(int,input().split())) # 순열

if N == 1:
    print('A')
else:
    ## 일단 첫수와 두번째 수를 비교하여 경우의 수를 찾아준다.
    first = arr.popleft()
    last = arr[-1]
    x = last // first
    s = last - first
    cal   = []
    for i in range(-200, 201):
        for j in range(-20000, 20001):
            if first * i + j == arr[0]:
                cal.append((i,j))
    print(cal)
    for j in range(1,N):
        now = arr.popleft() # 수를 뺀다.
        if arr:
            for c in cal:
                if now * c[0] + c[1] == list(arr)[0]:
                    pass
                else:
                    cal.remove(c)

    if len(cal) == 1:
        print(last * cal[0][0] + cal[0][1])
    elif not cal:
        print('B')
    else:
        print('A')

