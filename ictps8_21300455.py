'''
Junyoung Oh
PA08. Ski Game
'''
dp = dict()
n = int(input())
get_input = lambda : [int(i) for i in input().split()]
alt = [get_input() for i in range(n)]

def longest(coord):
    disRight = disLeft = disDown = disUp = 0
    row, col = coord

    if coord in dp: return dp[coord]
    
    if col+1 < n and alt[row][col] > alt[row][col+1]:
        disRight += longest((row, col+1)) + alt[row][col] - alt[row][col+1]
    if col-1 >= 0 and alt[row][col] > alt[row][col-1]:
        disLeft += longest((row, col-1)) + alt[row][col] - alt[row][col-1]
    if row+1 < n and alt[row][col] > alt[row+1][col]:
        disDown += longest((row+1, col)) + alt[row][col] - alt[row+1][col]
    if row-1 >= 0 and alt[row][col] > alt[row-1][col]:
        disUp += longest((row-1, col)) + alt[row][col] - alt[row-1][col]
    
    maxDis = max(disRight, disLeft, disDown, disUp)
    dp[coord] = maxDis
    
    return maxDis

maxDis = 0
for row in range(n):
    for col in range(n):
        if maxDis < longest((row, col)):
            maxDis = longest((row, col))

print(maxDis)
