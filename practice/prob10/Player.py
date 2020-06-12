class Player:
    UPPER = 6
    LOWER = 7
    
    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER + self.LOWER)]
        self.used = [False for i in range(self.UPPER + self.LOWER)]
        
    def setScore(self, score, index):
        self.scores[index] = score
        self.setAtUsed(index)
    
    def getUpperScore(self):
        uppertotal = 0
        for i in range(self.UPPER):
            uppertotal += self.scores[i]
        return uppertotal
    
    def getLowerScore(self):
        Lowertotal = 0
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            Lowertotal += self.scores[i]
        return Lowertotal
    
    def getUsed(self, index):
        return self.used[index]

    def setAtUsed(self, index):
        self.used[index] = True

    def getTotalScore(self):
        if self.getUpperScore() > 63:
            return self.getUpperScore() + self.getLowerScore() + 25
        else:
            return self.getUpperScore() + self.getLowerScore()
    
    def toString(self):
        return self.name
    
    def allUpperUsed(self):
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True

    def allLowerUsed(self):
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            if self.used[i] == False:
                return False
        return True