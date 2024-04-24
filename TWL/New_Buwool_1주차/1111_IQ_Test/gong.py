# N <= 50,재귀로
# 수는 -100 <= X <=100 
# a 는 다음 수 //로 나눈 것까지 가능. b 는 a로 나눈 나머지
# N = 1,2 return A, 절댓값이 점점 더 작아지면 B_
# 문제는 음수. 1 2 3 번갈아서면 a음수  b는 양수거나 음수거나      
# x ax+b, x*a**2+a*b+b  
# x1 ax1-ax1+x2 ax2-ax1+x2    
# 1 2 a+2   
N = int(input())
n_lst = list(map(int,input().split()))

if N == 1:
    print('A')
elif N == 2:
    if n_lst[0] == n_lst[1]:
        print(n_lst[0])
    else:
        print('A')
else:
# 범위는 2번째 3번째 수가 정함. 특히 a
    if n_lst[1] == n_lst[0]:
        check =True
        for n in range(1,N):
            if n_lst[0] != n_lst[n]:
                check = False
                break
        if check:
            print(n_lst[0])
        else:
            print('B')
        # 이 포인트 빼먹음
    else:
        a = (n_lst[2]-n_lst[1])/(n_lst[1]-n_lst[0])
        b = n_lst[1]-a*n_lst[0]
        result = 0
        if a%1 != 0:
            print('B')
        else:

            for n in range(1,N):
                result = a*n_lst[n] + b
                if n < N-1:
                    if result !=n_lst[n+1]:
                        print('B')
                        break
            else:
                print(int(result))