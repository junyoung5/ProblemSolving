'''
JunyoungOh
Card Game
Lower bound reference: http://12bme.tistory.com/120
'''

cardNum = int(input())
deck = [int(input()) for i in range(cardNum)]

def BinarySearch(table, front, rear, newCard):
    while(rear-front > 0):
        m = (front + rear) // 2
        if table[m] < newCard:
            front = m + 1
        else:
            rear = m
    return rear

def LongestIS(deck, size):
    table = [0 for i in range(size)]
    scoreList = [0 for i in range(size)]
    score = 1
    
    table[0] = deck[0]
    scoreList[0] = score 
    for i in range(1, size):
        if (deck[i] < table[0]):
            table[0] = deck[i]
            scoreList[i] += 1

        elif (deck[i] > table[score-1]):
            table[score] = deck[i]
            score += 1
            scoreList[i] += score

        else:
            r = BinarySearch(table, -1, score-1, deck[i])
            table[r] = deck[i]
            scoreList[i] += r + 1

    return scoreList

scoreIncreasing = LongestIS(deck, len(deck))
scoreIncreasingReversed = LongestIS(list(reversed(deck)), len(deck))
scoreDecreasing = list(reversed(scoreIncreasingReversed))

maxScore = 0
for i in range(len(scoreIncreasing)):
    scoreCalculated = scoreIncreasing[i] + scoreDecreasing[i] - 1
    if maxScore < scoreCalculated:
        maxScore = scoreCalculated

print(maxScore)

    
