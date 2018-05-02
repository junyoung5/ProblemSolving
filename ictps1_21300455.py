'''
Junyoung Oh
Broken Hit Counter
'''

total = 0
ex = 0

InputInList = list(map(lambda x: int(x), str(int(input()))))

for i in reversed(InputInList):
    if i > 4:
        total += (i-1) * (9 ** ex)
    else:
        total += i * (9 ** ex)
    ex += 1
    
print(total)





