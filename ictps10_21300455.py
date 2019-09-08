'''
Junyoung Oh
Taekwondo
application of union find
'''
matchLst = []
playerNum = int(input())
gameNum = int(input())
get_match = lambda : [int(i) for i in input().split()]
for i in range(gameNum):
    matchLst.append(get_match())

class Graph:
    def __init__(self, V, matchLst):
        self.V = V
        self.matchNum = 0
        self.matchLst = matchLst
        self.opponent = [0] * (self.V+1)
        self.rank = [0] * (self.V+1)
        self.parent = [0]
        for i in range(1, self.V + 1):
            self.parent.append(i)

    def findRoot(self, v):
        if self.parent[v] == v:
            return v
        else:
            self.parent[v] = self.findRoot(self.parent[v])
            return self.parent[v]
        
    def findBoth(self, p1, p2):
        return self.findRoot(p1), self.findRoot(p2)
    
    def union(self, p1, p2):
        oppRoot, candRoot = self.findBoth(p1, p2)
        
        if oppRoot == candRoot:
            return
        
        if self.rank[oppRoot] > self.rank[candRoot]:
            self.parent[candRoot] = oppRoot
            
        elif self.rank[oppRoot] < self.rank[candRoot]:
            self.parent[oppRoot] = candRoot
            
        else:
            self.parent[candRoot] = oppRoot
            self.rank[oppRoot] += 1
        
    def isConflict(self):
        for i in self.matchLst:
            self.matchNum += 1
            p1rep, p2rep = self.findBoth(i[0], i[1])
 
            if p1rep == p2rep: print(self.matchNum); return
            
            if self.opponent[i[0]] == 0:
                self.opponent[i[0]] = self.findRoot(i[1])

            else:
                candTeamRep = self.opponent[i[0]]
                self.union(candTeamRep, i[1])

            if self.opponent[i[1]] == 0:
                self.opponent[i[1]] = self.findRoot(i[0])
                
            else:
                candTeamRep = self.opponent[i[1]]
                self.union(candTeamRep, i[0])


g = Graph(playerNum, matchLst)
g.isConflict()
print(g.parent)
print(g.opponent)
