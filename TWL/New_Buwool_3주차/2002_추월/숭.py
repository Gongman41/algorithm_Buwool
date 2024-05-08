# 첨에 덱써서 걍 하려다가 실패함
# 딕셔너리로 함 해보까?
n = int(input())

# 터널이라는 딕셔너리에 차가 들어온 순서대로 차의 이름을 key, 순서를 value로 넣음
tunnel = {}
for i in range(n):
    tunnel[input()]  = i

# 추월한 차의 대수를 셀 거야
cnt = 0
for j in range(n):
    # 터널에서 나온 차의 번호를 받아
    car_name = input()
    # 이 차가 터널에 들어갔을 때의 순서를 저장
    car_order = tunnel[car_name]
    # 터널 딕셔너리에서 이 차 정보 삭제
    del tunnel[car_name]
    # 삭제한 딕셔너리에서 values들을 보며 이 차가 들어갔을 때의 순서보다 더 앞의 순서 차량이 아직 딕셔너리에 남아있으면
    # 앞에 들어간 차가 나오지 않았는데 이 차가 먼저 나온 것이 되므로 추월했다고 봄
    for order in tunnel.values():
        if order < car_order:
            cnt += 1
            break
print(cnt)