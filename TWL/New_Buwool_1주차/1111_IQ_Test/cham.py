import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
# 숫자 세 개는 있어야 알 수 있음
# 다음 수가 여러 개일 경우에는 A를 출력하고, 다음 수를 구할 수 없는 경우에는 B
# 앞 수 * a + b
if N == 1:
    print('A')
elif N == 2:    # 숫자 두 개인 경우
    if arr[0] == arr[1]:    # 두 개가 같은 값인 경우
        print(arr[0])   # 그 다음도 계속 같은 값일 것..
    else:
        print('A')
else:
    if arr[0] - arr[1] == 0:
        a = 0
    else:
        a = (arr[1] - arr[2]) // (arr[0] - arr[1])

    b = arr[1] - arr[0] * a

    for i in range(N-1):   # 구한 a, b가 맞는지 확인하는 반복문
        next_num = arr[i] * a + b
        if next_num != arr[i+1]:    # 실제 값이랑 다르면
            print('B')
            break
    else:
        print(arr[-1] * a + b)
