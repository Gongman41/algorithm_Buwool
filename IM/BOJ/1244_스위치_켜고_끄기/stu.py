import sys
sys.stdin = open('input.txt')
# 스위치 개수 switch_num
switch_num = int(input())
# 스위치의 상태를 나타내는 배열 switch_list
temp = [0]
input_list = list(map(int, input().split()))
switch_list = temp + input_list
# 학생 수
student_num = int(input())
# 학생의 성별과 지급받을 숫자를 쌍으로 가진 배열
on_off_list = []
for _ in range(student_num):
    gender, special_num = map(int, input().split())
    on_off_list.append([gender, special_num])
# 해당 순서대로 실행
for on_off in on_off_list:
    if on_off[0] == 1:  # 남학생
        div = on_off[1] # 배수가 될 수
        for s in range(div, switch_num + 1, div):
            if switch_list[s] == 1:
                switch_list[s] = 0
            # 0이면 1로 변경
            else:
                switch_list[s] = 1
    else:   # 여학생
        now = on_off[1] # 여학생이 받은 스위치의 번호
        on_off_list = [now] # 해당 번호를 켜고킬 리스트에 추가
        for i in range(1, switch_num // 2 + 1):
            if now-i >= 1 and now+i <= switch_num: # 스위치 인덱스 안에 양쪽 수가 있을 때
                # 해당 양쪽 수들이 서로 같은 상태일때
                if switch_list[now-i] == switch_list[now+i]:
                    on_off_list.append(now-i)
                    on_off_list.append(now+i)
            else:
                break
        for on_off in on_off_list:
            if switch_list[on_off] == 1:
                switch_list[on_off] = 0
            else:
                switch_list[on_off] = 1

print(*switch_list[1:])