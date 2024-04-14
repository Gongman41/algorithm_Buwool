def operator(idx, s):
    global maxi
    global mini

    if idx == N-1:
        maxi = max(s, maxi)
        mini = min(s, mini)
        return
    
    else:
        for i in range(N-1):
            if not visited[i]:
                visited[i] = 1
                tmp = s
                
                if op_lst[i] == 0:
                    tmp += A[idx+1]
                elif op_lst[i] == 1:
                    tmp -= A[idx+1]
                elif op_lst[i] == 2:
                    tmp *= A[idx+1]
                else:
                    if tmp > 0:
                        tmp //= A[idx+1]
                    else:
                        tmp = -(-tmp // A[idx+1])
                
                operator(idx+1, tmp)

                visited[i] = 0


N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
# +, -, * /

op_lst = []
for i in range(4):
    op_lst.extend([i]*op[i])
maxi = int(-1e9)
mini = int(1e9)
visited = [0 for _ in range(N-1)]
operator(0, A[0])    
print(maxi, mini)