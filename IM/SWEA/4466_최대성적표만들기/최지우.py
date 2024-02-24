import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    # score.sort(reverse=True)
    # result = sum(score[:K])
    # print(f'#{tc} {result}')

    sub = []
    for i in score:
        if not sub:
            sub.append(i)
        elif len(sub) < K:
            c = 0
            for j in range(len(sub)):
                if i >= sub[j]:
                    c += 1
                else:
                    sub.insert(c, i)
        else:
            for j in range(K):
                if i >= sub[j]:
                    i, sub[j] = sub[j], i
                else: break
    print(f'#{tc} {sum(sub)}')
            
