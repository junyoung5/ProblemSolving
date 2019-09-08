'''
Junyoung Oh
Step Function
'''
posList = []

fNum = int(input())
for i in range(fNum):
    fxCoor, fyCoor = [int(x) for x in input().split()]
    posList.append((fxCoor, fyCoor))

gNum = int(input())
for i in range(gNum):
    gxCoor, gyCoor = [int(x) for x in input().split()]
    posList.append((gxCoor, gyCoor))

p, q = [int(x) for x in input().split()]

posList.append((q,0)); posList.sort()

head = bag = 0; xPos = p; yPos= 0

while head < len(posList):
    if p >= posList[head][0]:
        if yPos < posList[head][1]:
            yPos = posList[head][1]
        head += 1
        
    elif q >= posList[head][0]:
        bag += (posList[head][0] - xPos) * yPos
        xPos = posList[head][0]
        if posList[head][1] > yPos:
            yPos = posList[head][1]
        head += 1
        
    else: break
    
bag += yPos

print(bag % 10007)
