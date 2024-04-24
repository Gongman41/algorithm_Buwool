n = int(input())
data = list(map(int, input().split()))

if n == 1: 
    print('B')
elif n == 2:
    print('A')
else:
  # 0, 1, 2번을 이용해 a와 b를 구함(이차방정식)
    if (data[0] - data[1] == 0):
        a = 0
    else:
        a = (data[1] - data[2]) // (data[0] - data[1])

    b = data[1] - data[0] * a

    # a와 b를 통해 예측값과 실제값을 비교. 만약 틀리다면 구할 수 없는 경우
    for i in range(n - 1):
        expect = data[i] * a + b  # 다음 예측값
        if (data[i + 1] != expect):  # 예측값과 실제가 다르다면
            print('B')
            exit()

    print(data[-1] * a + b)