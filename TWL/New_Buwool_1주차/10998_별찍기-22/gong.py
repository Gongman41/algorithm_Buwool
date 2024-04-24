def star(n):
    if n == 1:
        return
    elif n == 2:
        lst = ['*****','*','* ***','* * *','* * *','*   *','*****']
        return lst
    else:
        last_star = star(n-1)
        this_star = ['*'*(4*n-3),'*']
        
        for i in range(len(last_star)):
            if i == 0:
                last_star[i] = '* ' + last_star[i] + '**'
            elif i == 1:
                last_star[i] = '* ' + last_star[i] + ' ' * (len(last_star[i-1])-4) + '*'
            else:
                last_star[i] = '* ' + last_star[i] + ' *'
            
        this_star = this_star + last_star +['* '+' '*(4*n-7)+' *','*'*(4*n-3)]
        return this_star
N = int(input())
if N == 1:
    print('*')
else:
    stars = star(N)
    for starr in stars:
        print(starr)