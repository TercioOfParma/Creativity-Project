import random
VIRTUE_BOUND = 100 #The max is 100 for generation, but can exceed this, just as 0 is the minimum


class virtues:
    def __init__(self):
        self.fortitude = 0 #0
        self.justice = 0 #1
        self.temperance = 0 #2
        self.prudence = 0 #3
        self.faith = 0 #4
        self.hope = 0 #5
        self.charity = 0 #6
        self.requiredScore = 0  # Combines on death to see if the character succeeds
        self.inSin = True  # This determines if the person is in error
        self.selectedVirtue = 0
        self.selectVirtue()
    def selectVirtue(self):
        self.selectedVirtue = random.randrange(0,7)