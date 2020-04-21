class moralAction:
    def __init__(self, name, verb, kindOfAction, virtueOperatedOn):
        self.name = name
        self.verb = verb
        self.kindOfAction = kindOfAction  # stored as string, and then read into function to determine effect
        self.virtueOperatedOn = virtueOperatedOn  # The virtue modified by this

