import sys
sys.stdin = open('input.txt')


data = [list(map(int, input().split())) for _ in range(4)]
matrix = [[0] * 100 for _ in range(100)]
result = 0
for pos in data:
    for x in range(pos[0], pos[2]):
        for y in range(pos[1], pos[3]):
            # 몇번이 겹치든 한번만 칠할 거임.
            # 한번 칠해졌으면 더 칠 안함
            if matrix[x][y] == 0:
                # 칠한다
                matrix[x][y] = 1
                # 더한다.
                result += 1
print(result)