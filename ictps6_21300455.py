'''
Junyoung Oh
electricty Poles
'''
polLst = []

polNum, amplNum = [int(i) for i in input().split()]

for i in range(polNum):
    polLst.append(int(input()))
polLst.sort()

posMax = polLst[-1]; posMin = polLst[0]
MaxOfMin = -(-(posMax-posMin) // (amplNum - 1))

start = 0; end = MaxOfMin
while(True):
    
    if start+1 == end: M = end
    else: M = (start+end) // 2

    tail = head = realAmplN = 0
    while(head < (len(polLst))):
        
        if polLst[head] - polLst[tail] >= M:
            tail = head
            realAmplN += 1
        head += 1
    
    if realAmplN >= amplNum - 1 :
        if start == end : print(start); break
        start = M
        
    else :
        if start== end: print(start); break
        end = M - 1

    
            
        
