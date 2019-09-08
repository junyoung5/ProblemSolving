numDisc, dEnd= [int(x) for x in input().split()]

rodOne= [int(x) for x in input().split()]; del rodOne[0] 
rodTwo = [int(x) for x in input().split()]; del rodTwo[0] 
rodThree = [int(x) for x in input().split()]; del rodThree[0]  

L = [0] * 101
for i in rodOne: L[i] = 1; for i in rodTwo: L[i] = 2; for i in rodThree: L[i] = 3

cnt = 0; dFrom = L[numDisc]

while(numDisc > 0):
    dFrom = L[numDisc]
    if dFrom == dEnd: numDisc -= 1; continue
    else: cnt += 2 ** (numDisc-1); dEnd = dFrom ^ dEnd; numDisc -= 1
    
print(cnt)

