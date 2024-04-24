# 문제를 잘 읽으면 갑자기 y(다음수) = x(지금수)*a + b 라는 규칙이 나옴
# 3개의 수를 가지고 2개의 방정식을 만들 수 있음 => 이걸로 a와 b를 구해 규칙 찾기

n = int(input())
data = list(map(int, input().split()))

# 예외 케이스가 좀 많은데,, 잘 따져봐야 함

# 숫자가 1개만 주어지면 규칙 파악 불가... 아무 숫자나 와도 됨
if n == 1:
    print('A')
elif n == 2:
    # data에 있는 모든 수에 이 규칙이 통해야 함
    if data[0] == data[1]:  # 주어진 두 개가 같다면 그 다음 것도 당연히 똑같은 숫자임
        print(data[0])
    else:   # 두 개가 다르면 규칙 파악 불가. 암거나 와도 됨
        print('A')
else:
    if data[0] == data[1]:  # 기울기의 분모가 0이 되기 때문에 예외
        a= 0
    else:
        a = (data[2] - data[1]) // (data[1] - data[0])  # 기울기 구하는 식

    b = data[1] - data[0] * a   # y절편 구하기

    # a와 b를 통해 얻은 예측값과 실제값을 비교!! 다르다면.. 걍 이상한 식!
    for i in range(n-1):
        target = data[i] * a + b    # 예측 값
        if data[i+1] != target:
            print('B')
            break
    else:
        print(data[-1] * a + b) # 오 올바른 식이구나~ 규칙을 통해 다음 값 구함