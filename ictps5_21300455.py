'''
JunyoungOH
polyomino
test10
'''

baseBoard = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
valLst = []
sizeLst = []
posLst = []
idLst = []

# number of Polyomino
n = int(input())

# get input for size and tetris.
for i in range(n):
    sizeLst.append([int(x) for x in input().split()])
    for y in range(sizeLst[i][0]):
        valLst.append([int(x) for x in input().split()])
    posLst.append(valLst)
    valLst = []

#make ID list: (id, w, h, (x,y))
for i in range(len(sizeLst)):
    idLst.append([i+1, sizeLst[i][0], sizeLst[i][1], [0,0]])

#find_candidate
def find_candidate(m):
    candidateLst = []
    for w in range(4):
        for h in range(4):
            if h + m[1] <= 4 and w + m[2] <= 4:
                candidateLst.append([h,w])

    return candidateLst

def find_valPos(m):
    global posLst
    valPos = []
    if m[0] == 1: valPos = posLst[0]
    elif m[0] == 2: valPos = posLst[1]
    elif m[0] == 3: valPos = posLst[2]
    elif m[0] == 4: valPos = posLst[3]
    elif m[0] == 5: valPos = posLst[4]
    return valPos

def cleanBoardIn(bx, by, x, y, candidate):
    global baseBoard
    #print("X Y:", x , y)
    for y in range(y, 0):
        for x in range(x, 0):
            bx += x; by += y
            baseBoard[by][bx] -= valPos[y][x]
            #print("celan", m, "   ", baseBoard) #dbg
            bx, by = candidate[0], candidate[1]
            
def cleanBoard(m):
    global baseBoard
    for y in range(4):
        for x in range(4):
            if baseBoard[y][x] == m[0]:
                baseBoard[y][x] = 0


def make_overlap(m, candidate):
    global baseBoard
    
    valPos = find_valPos(m)
    bh, bw = candidate[0], candidate[1]
    for h in range(m[1]):
        for w in range(m[2]):
            bh += h; bw += w
            
            if valPos[h][w] == 0:
                baseBoard[bh][bw] = baseBoard[bh][bw]
            
            elif baseBoard[bh][bw] == 0 and valPos[h][w] > 0:
                baseBoard[bh][bw] = m[0]
                #print("add  ", m, "   ", baseBoard) #dbg

            elif baseBoard[bh][bw] > 0 and valPos[h][w] > 0:
                cleanBoard(m)
                return False
            
            bh, bw = candidate[0], candidate[1]
            
    return True

def get_msg(is_fitted, is_empty):
    if is_fitted:
        if is_empty:
            return "Success"
        return "OK"
    return "Failure"


def permutation(lst, success = False, level = 0):
    if success: return success
    
    for z in range(len(lst)):
        candL = find_candidate(lst[z])
        m , remLst = lst[z], lst[:z] + lst[z+1:]
        is_empty = len(remLst) == 0
        for i in range(len(candL)):
            is_fitted = make_overlap(m, candL[i])
            
            if is_fitted:
                success = permutation(remLst, is_empty, level + 1)
                if success: break
                cleanBoard(m)
        if success: break
    return success

def is_full():
    global baseBoard
    for i in range(4):
        for z in range(4):
            if baseBoard[i][z] == 0: return False
    return True

if permutation(idLst) and is_full():
    for y in range(4):
        for x in range(4):
            print(baseBoard[y][x], end = " ")
        print(' ')
else:
    print("No solution possible")
