import sys
sys.stdin = open('input.txt')
T = 10

def gogo(srt): #들어가서 갈 곳에서 이전에 가야되는 곳들을 다 가서 지금 하나 남음 -> 출발
    if line_dict.get(srt) != None : #스택에 지금위치 넣고 결과값에  append. 그리고 갈곳의 이전갈곳카운트 -1
        n = 0
        for i in line_dict[srt]:

            if serveral_count[i] == 1:
                stack.append(srt)
                result.append(i)
                serveral_count[i] -= 1
                gogo(i)
            elif serveral_count[i] > 1:
                serveral_count[i] -= 1
                line_dict[srt][n] = 0
            n += 1
    if stack:# 위에 끝났다. stack에 저장된 이전 위치로 이동.원위치면 그냥 끝
        gogo(stack.pop())

        
for tc in range(1,T+1):
    V,E = map(int,input().split())
    lst = list(map(int,input().split()))
    line_dict = {} #간선  연결 딕셔너리
    serveral_count = [0]*(V+1)#목적지 언급 수
    start_list = [] #출발할 곳
    result = []
    stack = []
    for i in range(E):
        serveral_count[lst[2 * i + 1]]+=1 #목적지 언급되면 +1
        if line_dict.setdefault(lst[2*i],[lst[2*i+1]]) != [lst[2*i+1]]:#키에 값이 안들어 가 있으면 여기서 넣고 있으면 다른 값이 반환돼서 append
            line_dict[lst[2*i]].append(lst[2*i+1]) #간선 정보 넣기
    for i in range(1,len(serveral_count)):
        if serveral_count[i] == 0: #0이면 출발지
            start_list.append(i)
    for start in start_list:
        result.append(start)
        gogo(start)
    print(f'#{tc} ',end = '')
    print(*result)
        
    
        
            



