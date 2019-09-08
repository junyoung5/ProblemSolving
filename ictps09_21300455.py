'''
Junyoung Oh
Bulldozer
reference: Professor Shin
'''
n, d, m = [int(i) for i in input().split()]
schedule = [int(i) for i in input().split()]
schedule.sort()

def isAvailable(schedule, k):
    
    tDay = -1; idx = 0; delayed = 0
    delay = [0] * m
    
    while idx < m:
        newDay = schedule[idx] + delay[idx]

        if tDay != newDay: 
            bullNum = k; tDay = newDay
            idx -= delayed; delayed = 0; 
            
        if tDay > n: return False

        if bullNum > 0 : bullNum -= 1

        elif delay[idx] == d: return False
        
        else: 
            delay[idx] += 1
            delayed += 1

        if idx == m-1 and delayed > 0:
            idx -= delayed-1  #delay - 1 because we subtract before increase index
    
        else: idx+=1

    return True

def binary_search(schedule, lower, upper):
    
    if lower == upper:
        print((lower+upper)//2)
        return True
    k = (lower + upper) // 2
    flag = isAvailable(schedule, k)
    if flag == True:
        binary_search(schedule, lower, k)
    else:
        binary_search(schedule, k+1, upper)

lower = 1; upper = m       
binary_search(schedule, lower, upper)
