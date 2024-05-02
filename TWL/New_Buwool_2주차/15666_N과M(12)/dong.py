import sys
sys.stdin = open('input.txt')
'''
N개의 자연수와 자연수 M이 주어졌을 때, 해당 수열을 모두 구함
중복되는 수열을 여러번 출력하면은 안된다.
1. 같은 수를 여러번 골라도 된다.
2. 고른 수열은 비 내림차순 이어야 한다.
첫 줄에 N, M이 주어지고 (n은 원소의 개수, m은 수열의 길이)
그럼 재귀로 풀 수 있을 것 같다.
기저조건 : 만약 지금 길이가 m과 같아지면 return
아니라면, 재귀에 들어간 숫자만큼 돌려준다.
만약 해당 숫자를 방문하지 않았다면
더해주고, 재귀, 빠져나오면 숫자 빼주기 (리스트를 정렬해서 받음)
'''

n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
result = []

def solution(now):
    if len(result) == m:
        print(*result)
        return
    visited = 0
    for i in range(now, n):
        if visited != numbers[i]:
            result.append(numbers[i])
            visited = numbers[i]
            solution(i)
            result.pop()

solution(0)

    

