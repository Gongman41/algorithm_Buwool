def back_tracking(start, current_sequence):
    # 지금까지 만든 수열의 길이가 m을 만족한다면! 굳이 주어진 자연수의 끝까지 안 봐도 됨
    if len(current_sequence) == m:
        # 현재 수열이 조건을 만족하기 때문에 서브 수열 리스트에 넣음
        sub_sequences.append(current_sequence)
        return

    # for문을 돌며 시작점을 정해주어 수열의 각 숫자들이 주어진 자연수를 중복할 수 있도록 한다.
    # 새로운 k번째의 숫자가 수열에 들어갈 때마다 처음부터 끝까지의 모든 n개에 자연수를 접근할 수 있도록 함
    # back_traking의 첫번째 인자가 중요 !!!! (여기서는 중복 가능하게 만든거임 -> visited 처리 ㄴㄴ)
    for i in range(start, len(sequence)):
		    # i를 재귀함수의 start로 넣어줘서 내림차순이 되지 않도록 함
        back_tracking(i, current_sequence + [sequence[i]])

# n개의 자연수, 길이가 m인 서브수열
n, m = map(int, input().split())

# 자연수들을 입력받는데 중복을 제거한 후 list로 만듦
sequence = list(set(map(int, input().split())))
# 비내림차순,, 오름차순으로 만들어야 하니까 먼저 값을 정렬해놓으면 어차피 순서대로 고르므로.. 무조건 비내림차순이다
sequence.sort()
# 길이가 m인 서브 수열을 저장할 리스트
sub_sequences = []

# 백트래킹을 통해 길이가 m인 서브 수열을 찾을 거임
back_tracking(0, [])

# 서브 수열 출력
for sub in sub_sequences:
    print(*sub)
