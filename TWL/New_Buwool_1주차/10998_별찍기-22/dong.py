'''
1 : 
* 1
2 :
2 * 4 - 1
7 7 - N
***** 5
* 1
* *** 5
* * * 5 
* * * 5
*   * 5
***** 5
3 :
3 * 4 - 1
11 h - 2
********* 9
*         9
* ******* 9
* *     * 9
* * *** * 9 
* * * * * 9
* * * * * 9
* *   * * 9
* ***** * 9
*       * 9
********* 9
'''

def draw(n, y, x):
    star = '*'
    if n == 1:
        stars[x][y] = star
        stars[x+1][y] = star
        stars[x+2][y] = star
        return
    else:
        for i in range(4 * n - 4):
            stars[x][y] = '*'
            y -= 1
        for _ in range(4 * n - 2):
            stars[x][y] = '*'
            x += 1
        for _ in range(4 * n - 4):
            stars[x][y] = '*'
            y += 1
        for _ in range(4 * n - 4):
            stars[x][y] = '*'
            x -= 1

        stars[x][y] = '*'
        stars[x][y-1] = '*'
        draw(n-1, y-2, x)
        
N = int(input())

if N == 1:
    print('*')
else:
    width = 4 * N - 3
    height = 4 * N - 1
    stars = [['' for _ in range(width)] for _ in range(height)]
    draw(N, width-1, 0)
    for star in stars:
        print(''.join(' ' if char == '' else '*' for char in star).rstrip())
