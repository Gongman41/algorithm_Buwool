import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1, N+1):
    result = ''
    for n in str(i):
        if n == '3':
            result += '-'
        elif n == '6':
            result += '-'
        elif n == '9':
            result += '-'
    if not result:
        result = i  
    
    print(result, end = ' ')
