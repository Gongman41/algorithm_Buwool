n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    array = [0] * (n+1)
    array[1] = 1
    array[2] = 2
    for i in range(3, n+1):
        # 파이썬의 int는 메모리 4바이트 아님. 기본적으로 몇십만 바이트를 사용하기때문에 수의 크기가 커질수록 자릿수에 비례하는 만큼 메모리가 커짐
        # 미리 나눠 저장하여 메모리 초과 방지
        
        # 00, 1을 자리수에 맞게(00은 n-2, 1은 n-1) 맨 뒤에 갖다 붙이면 n+2가 나옴ㅋㅋ
        array[i] = (array[i-2] + array[i-1]) % 15746
    print(array[n])