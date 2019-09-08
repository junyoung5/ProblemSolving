'''
JunyoungOh
Ballon
'''
candList = []; inputList = []

get_data = lambda : [int(x) for x in input().split()]
touchingDis = lambda currX, prevX, prevR : (currX-prevX)**2 / (4*prevR)

for i in range(int(input())):
    inputList.append(get_data())

candList.append(inputList[0])
print("%0.3f" % inputList[0][1])

for head in range(1, len(inputList)):
    currX, currR = inputList[head][0], inputList[head][1]

    while(candList != []):
        prevX, prevR= candList[-1][0], candList[-1][1]
        currR = min(touchingDis(currX, prevX, prevR), currR)

        if currR < prevR: break
        else: candList.pop()

    print("%0.3f" % currR)
    candList.append([currX, currR])




        

    
        
