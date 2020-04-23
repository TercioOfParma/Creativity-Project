import random
VIRTUE_BOUND = 100 #The max is 100 for generation, but can exceed this, just as 0 is the minimum


class virtues:
    def __init__(self):
        self.fortitude = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND) #0
        self.justice = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND)  #1
        self.temperance = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND)  #2
        self.prudence = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND)#3
        self.faith = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND)#4
        self.hope = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND)#5
        self.charity = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND)#6
        self.requiredScore = random.randrange(-1 * VIRTUE_BOUND,VIRTUE_BOUND) # Combines on death to see if the character succeeds
        self.inSin = True  # This determines if the person is in error
        self.selectedVirtue = 0
        self.totalScore = 0
        self.selectVirtue()
    def selectVirtue(self):
        self.selectedVirtue = random.randrange(0,4)
    def spliceCharacter(self, person1, person2): #This is for subsequent generations
        self.fortitude = person1.virtue.fortitude
        self.prudence = person1.virtue.prudence
        self.temperance = person2.virtue.temperance
        self.justice = person2.virtue.justice
    def generateVirtueScore(self):
        self.totalScore = abs(self.fortitude) + abs(self.justice) + abs(self.temperance) + abs(self.prudence) +  abs(self.faith) + abs(self.hope) + abs(self.charity)
        return self.totalScore
