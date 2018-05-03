'''
Junyoung Oh
ictps2 Lazy Spider
2018.03.12
'''

foodChunk = {}
Position = []

n, k = [int(x) for x in input().split()]
k = k * 2

for i in range(n):
    chunk, pos = [int(x) for x in input().split()]
    Position.append(pos)
    foodChunk[pos] = chunk
    
Position.sort()

tail = head = bag = maxBag =  0

while(head < len(Position)):
    
    if Position[head] - Position[tail] <= k: 
        bag += foodChunk[Position[head]]
        maxBag = max(bag, maxBag)
        head += 1
        
    else:
        bag -= foodChunk[Position[tail]]
        tail += 1
        
print (maxBag)
