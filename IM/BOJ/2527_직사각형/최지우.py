import sys
sys.stdin = open('input.txt')

while True:
    try:
        x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
        
        # case (d)
        if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
            print('d')
            continue
    
        elif x1==p2 or x2==p1:
            # case (c)
            if q1==y2 or q2==y1:
                print('c')
                continue
            # case (b)
            else:
                print('b')
                continue
        elif q1==y2 or q2==y1:
            print('b')
            continue
    
        # case (a)
        else:
            print('a')
            continue

    except:
        break
'''

'''