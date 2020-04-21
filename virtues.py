import random
VIRTUE_BOUND = 100 #The max is 100 for generation, but can exceed this, just as 0 is the minimum


class virtues:
    def __init__(self):
        self.fortitude = 0 #1
        self.justice = 0 #2
        self.temperance = 0 #3
        self.prudence = 0 #4
        self.faith = 0 #5
        self.hope = 0 #6
        self.charity = 0 #7
        self.requiredScore = 0  # Combines on death to see if the character succeeds
        self.inSin = False  # This determines if the person is in error
        self.selectedVirtue = 0
        self.selectVirtue()
    def selectVirtue(self):
        self.selectedVirtue = random.randrange(1,7)