N = int(input())

h = (N*3)+(N-1)
w = h-2
L_res, R_res, final_res = '', '', ''

# N = 1인 경우 예외처리
if N==1:
    print('*')

else:
    numOddL = 0
    ### Top Left ###
    for i in range((h//2)+1):	# 현재 지나는 행 = i
        if i%2 == 0:    # 홀수행 - 별 출력이 공백보다 빈번함
            if numOddL == 0: # 첫번째 행
                L_res += '*'*((w+1)//2)
                numOddL += 1 
            else:     # =3, 5, 7.. 번째 행
                exclude_max = i-1  # 제외되는 idx 중 제일 큰 값
                ex_tmp = []
                for j in range(1, exclude_max+1, 2): # 이 행에서 제외되는 idx 수만큼
                    ex_tmp.append(j)
                star_str = ''
                for k in range((w+1)//2):
                    if k not in ex_tmp:
                        star_str += '*'
                    else:
                        star_str += ' '
                L_res += star_str   
                numOddL += 1
        
        else:   # 짝수행 - 공백이 별 출력보다 빈번함
            numStar = i
            star_tmp = []		# 별이 찍히는 idx
            for j in range(0, i, 2):    # 2, 4, 6.. 번째 행
                star_tmp.append(j)
            star_str = ''
            for k in range((w+1)//2):
                if k not in star_tmp:
                    star_str += ' '
                else:
                    star_str += '*'
            L_res += star_str
        L_res += '\n'

    ### Bottom Left ###
    for i in range(h-(h//2)-1):
        L_res += L_res.split('\n')[(h-(h//2)-1)-(i+1)] + '\n'

    ### Top Right ###
    for i in range((h//2)+1):
        tmp = L_res.split('\n')[i]
        tmp = list(tmp)
        del tmp[0]
        del tmp[0]
        tmp.reverse()
        
        if i%2 == 0:
            R_res += '*'
        else:
            R_res += ' '
        for j in range(len(tmp)):
            R_res += tmp[j]
        R_res += '\n'

    ### Bottom Right ###
    for i in range((h//2)):
        tmp = L_res.split('\n')[((h//2)+1)-(i+2)]
        tmp = list(tmp)
        del tmp[-1]
        tmp.reverse()
        for j in range(len(tmp)):
            R_res += tmp[j]
        R_res += '\n'

	### Final 결과 정리 ###
    for i in range(h+1):
        line2 = ''  # 둘째 줄 예외처리
        if i==1:    # 둘째 줄은 * 이후에 공백이 필요없음!!! 
            line2 += L_res.split('\n')[i]
            line2 += R_res.split('\n')[i]
            line2 = list(line2)
            for _ in range(w-1):
                del line2[1]
            final_res += line2[0]
            final_res += '\n'
    
        else:
            final_res += L_res.split('\n')[i]
            final_res += R_res.split('\n')[i]
            final_res += '\n'
    
    final_res = final_res.rstrip('\n')
    print(final_res)
