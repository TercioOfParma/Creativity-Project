from virtues import virtues
from action import moralAction
import random
from Markov import Markov

intention = ['After some thought, ', 'Intentionally, ', 'After deliberation, ', 'By design, ', 'Wittingly, ']
tempted = ['After temptation, ', 'After being enticed, ', 'Wooed by his thoughts, ', 'Seduced by temptation, ', 'Following his desires, ']
repentence = [' Tears their clothes', ' repents of their sins', ' weeps for their wrongdoings', ' cries for forgiveness', ' ask for clemency from God']
# Virtues
fortitude = 'FORTITUDE'
justice = 'JUSTICE'
temperance = 'TEMPERANCE'
prudence = 'PRUDENCE'
faith = 'FAITH'
hope = 'HOPE'
charity = 'CHARITY'

AGE_WEIGHT = 20
SIN_WEIGHT = 3

FORTITUDE = 0
JUSTICE = 1
TEMPERANCE = 2
PRUDENCE = 3
FAITH = 4
HOPE = 5
CHARITY = 6

# Action Types
INTENTIONAL_INTERIOR_EVIL = 'INTENTIONAL_INTERIOR_EVIL'
INTENTIONAL_EXTERIOR_EVIL = 'INTENTIONAL_EXTERIOR_EVIL'
VIOLENCE = 'VIOLENCE'
FORNICATION = 'FORNICATION'
LOVE_IN_MARRIAGE = 'LOVE_IN_MARRIAGE'
REPENTENCE = 'REPENTENCE'
INTENTIONAL_INTERIOR_GOOD = 'INTENTIONAL_INTERIOR_GOOD'
INTENTIONAL_EXTERIOR_GOOD = 'INTENTIONAL_EXTERIOR_GOOD'
DECEPTION = 'DECEPTION'
STEALING = 'STEALING'
THANKSGIVING = 'THANKSGIVING'

fortitudelist = ['Hard', 'Tough', 'Enduring', 'Longsuffering', 'Adamantine' , 'Faithful', 'Devoted', 'Dedicated']
justicelist  = ['Just', 'Litigious', 'Fair', 'Even-handed', 'Honourable','Benevolent', 'Magnanimous', 'Philanthropic']
temperancelist  = ['Temperant', 'Sober', 'Ascetic', 'Pure of Heart', 'Disciplined', 'Controlled', 'Austere', 'Simple']
prudencelist  = ['Prudent', 'Wise', 'Scholastic', 'Reader', 'Bright', 'Trusting', 'Sagacious', 'Cautious']
class person:
    def __init__(self, name, age, markov, isBorn, Parent=None):
        self.virtue = virtues()
        self.age = age
        self.ageLimit = random.randrange(60, 80)
        self.sinLimit = random.randrange(1,40) #St Alphonsus Ligouri is quite keen to emphasise a single sin can doom
        self.sinCount = 1
        self.sinList = ""
        self.isAlive = True
        self.score = 0
        #print(name)
        self.name = name + self.title()
        self.lineage = self.begetting(markov)
        if(isBorn == False):
            self.life = self.lineage + self.name + '\n'
        else:
            self.born(markov, Parent)
        self.actions = []  # A list that contains all of the actions

    def born(self, markov, parent):
        self.life = parent.lineage + parent.name + ' begot ' +  self.name + '\n'
        self.lineage = parent.lineage + ' ' + parent.name
        #print("FORNICATION " + self.life)
    def death(self):
        self.score = self.virtue.generateVirtueScore() + (self.sinCount * SIN_WEIGHT) + (self.age * AGE_WEIGHT)
        if not self.virtue.inSin:
            self.life = self.life + self.name + " dies a happy death" + '\n'
        else:
            self.life = self.life + self.name + " dies an unhappy death" + '\n'
    def outputLife(self):
        fp = open("story/" + self.name + '.txt', 'w')
        fp.write(self.life)
        fp.write('\n\n FINAL SCORE: ' + str(self.virtue.generateVirtueScore()))
        fp.close()
    def title(self):
        adjective = random.randrange(0,8)
        if self.virtue.selectedVirtue == FORTITUDE:
            return " The " + fortitudelist[adjective]
        if self.virtue.selectedVirtue == JUSTICE:
            return " The " + justicelist[adjective]
        if self.virtue.selectedVirtue == TEMPERANCE:
            return " The " + temperancelist[adjective]
        if self.virtue.selectedVirtue == PRUDENCE:
            return " The " + prudencelist[adjective]
    def begetting(self, markov):
        numberOfGenerations = random.randrange(1,20)
        beget = ''
        i = 0
        while i < numberOfGenerations:
            names = markov.New()
            beget = beget + names + ' begot '
            i += 1

        return beget

    def generateActions(self):
        self.actions.append(moralAction('Repentence', 'repents of his evil', REPENTENCE, CHARITY))

        #Prudence

        #POSITIVE
        self.actions.append(moralAction('Memory', 'remembers the moral law', INTENTIONAL_INTERIOR_GOOD, PRUDENCE))
        self.actions.append(moralAction('Understanding', 'comes to understand the moral law', INTENTIONAL_INTERIOR_GOOD, PRUDENCE))
        self.actions.append(moralAction('Docility', 'listens to the wisdom of ', INTENTIONAL_EXTERIOR_GOOD, PRUDENCE))
        self.actions.append(moralAction('Shrewdness', 'quickly solves a problem for ', INTENTIONAL_EXTERIOR_GOOD,PRUDENCE))
        self.actions.append(moralAction('Reason', 'applies the moral law to his life.', INTENTIONAL_INTERIOR_GOOD,PRUDENCE))
        self.actions.append(moralAction('Foresight', 'avoids a previous stumbling block. ', INTENTIONAL_INTERIOR_GOOD,PRUDENCE))
        self.actions.append(moralAction('Circumspection', 'takes stock of his situation ', INTENTIONAL_INTERIOR_GOOD, PRUDENCE))
        self.actions.append(moralAction('Caution', 'dodges a previous imperfection ', INTENTIONAL_EXTERIOR_GOOD,PRUDENCE))

        #NEGATIVE
        self.actions.append(moralAction('Precipitation', 'rashly ignores the counsel of ', INTENTIONAL_EXTERIOR_EVIL, PRUDENCE))
        self.actions.append(moralAction('Inconsideration', 'completes his work imperfectly ', INTENTIONAL_INTERIOR_EVIL, PRUDENCE))
        self.actions.append(moralAction('Inconstancy', 'refuses the difficult counsel of ', INTENTIONAL_EXTERIOR_EVIL, PRUDENCE))
        self.actions.append(moralAction('Negligence', 'neglects his work ', INTENTIONAL_INTERIOR_EVIL, PRUDENCE))
        self.actions.append(moralAction('Carnal Prudence', 'uses his cunning to acquire money beyond his needs ', INTENTIONAL_INTERIOR_EVIL,PRUDENCE))
        self.actions.append(moralAction('Craftiness', 'abuses the law to his gain ', INTENTIONAL_INTERIOR_EVIL, PRUDENCE))
        self.actions.append(moralAction('Guile', 'lies to ', DECEPTION, PRUDENCE))
        self.actions.append(moralAction('Fraud', 'Defrauds ', INTENTIONAL_EXTERIOR_EVIL,PRUDENCE))


        #JUSTICE

        #POSITIVE
        self.actions.append(moralAction('Commutative', 'resolves the legal case of ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Legal', 'visits the imprisoned ', INTENTIONAL_INTERIOR_GOOD,JUSTICE))
        self.actions.append(moralAction('Distributive', 'distributes alms to the poor. ', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Restitution', 'repays a loan from ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Religion', 'prays without ceasing', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Devotion', 'fulfils a novena', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Adjuration', 'swears an oath to follow the natural moral law ', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Piety', 'lives in complete obedience to his parents', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Patriotism', 'serves a term in the army', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Observance', 'does not miss Mass', INTENTIONAL_INTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Dulia', 'develops a strong devotion to Saint ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE)) #randomly generate a name
        self.actions.append(moralAction('Obedience', 'renders unfaltering service to ', INTENTIONAL_EXTERIOR_GOOD,JUSTICE))
        self.actions.append(moralAction('Diligence', 'fulfils all his work to ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Thanksgiving', 'is thankful to ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Just Vindication', 'brutally puts an end to the evil of ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Honesty', 'reveals his sin to ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Friendship', 'makes friends with ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))
        self.actions.append(moralAction('Liberality', 'Gives alms', INTENTIONAL_INTERIOR_GOOD,JUSTICE))
        self.actions.append(moralAction('Epieikeia', 'meditates on the moral law ', INTENTIONAL_EXTERIOR_GOOD, JUSTICE))

        #NEGATIVE
        self.actions.append(moralAction('Commutative', 'unnecessarily supplicates to ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Murder', 'murders ', VIOLENCE, JUSTICE))
        self.actions.append(moralAction('Mutilate', 'cuts the arm off of ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Theft', 'steals from ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Robbery', 'beats and robs from ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Judgement', 'looks down their nose at ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('False Accusation', 'calumniates ', DECEPTION, JUSTICE))
        self.actions.append(moralAction('Perjury', 'swears a false oath ', INTENTIONAL_INTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Contumely', 'attacks the reputation of ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Detraction', 'tells everybody publically about the secrets of ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Murmuring', 'quietly tells secrets about ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Derision', 'mocks ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Malediction', 'curses ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Usury', 'loansharks ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Illicit Adjuration', 'swears an unfulfilable oath.', INTENTIONAL_INTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Superstition', 'honours the demon ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE)) #generate a name
        self.actions.append(moralAction('Idolatry', 'worships the idol ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))  #generate a name
        self.actions.append(moralAction('Divination', 'casts a spell to gain money ', INTENTIONAL_INTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Tempting God', 'tempts God', INTENTIONAL_INTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Sacrilege', 'commits sacrilege', INTENTIONAL_INTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Simony', 'purchases relics of St ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE)) #generate a name
        self.actions.append(moralAction('Disobedience', 'disobeys  ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Vengefulness', 'desires vengence against ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Lying', 'lies to ', DECEPTION,JUSTICE))
        self.actions.append(moralAction('Simulation', 'commits sin to deceive ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Boasting', 'boasts to ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Ingratitude', 'ignores the good deed of ', INTENTIONAL_EXTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Irony', 'makes an effort to appear lowly to others', INTENTIONAL_INTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Adulation', 'sucks up to ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Litigious', 'excessively sues ', INTENTIONAL_EXTERIOR_EVIL,JUSTICE))
        self.actions.append(moralAction('Avarice', 'chases money.', INTENTIONAL_INTERIOR_EVIL, JUSTICE))
        self.actions.append(moralAction('Prodigality', 'wastes money ', INTENTIONAL_INTERIOR_EVIL, JUSTICE))

        #FORTITUDE


        #Positive
        self.actions.append(moralAction('Magnanimity', 'plans great things ', INTENTIONAL_INTERIOR_GOOD, FORTITUDE))
        self.actions.append(moralAction('Magnificence', 'builds a church.', INTENTIONAL_INTERIOR_GOOD, FORTITUDE))
        self.actions.append(moralAction('Patience', 'suffers admirably with an illness', INTENTIONAL_INTERIOR_GOOD,FORTITUDE))
        self.actions.append(moralAction('Perserverence', 'grows virtue despite a great ailment', INTENTIONAL_INTERIOR_GOOD, FORTITUDE))
        self.actions.append(moralAction('Longanimity', 'waits to commit a great good', INTENTIONAL_INTERIOR_GOOD, FORTITUDE))
        self.actions.append(moralAction('Mortification', 'fasts intensely ', INTENTIONAL_INTERIOR_GOOD, FORTITUDE))

        #Negative

        self.actions.append(moralAction('Fear', 'fears for his mortality ', INTENTIONAL_INTERIOR_EVIL,FORTITUDE))
        self.actions.append(moralAction('Fearlessness', 'meaninglessly risks his life. ', INTENTIONAL_INTERIOR_EVIL,FORTITUDE))
        self.actions.append(moralAction('Audacity', 'loses his temper at an angry lion ', INTENTIONAL_INTERIOR_EVIL,FORTITUDE))
        self.actions.append(moralAction('Presumption', 'dwells on his own self sufficiency ', INTENTIONAL_INTERIOR_EVIL, FORTITUDE))
        self.actions.append(moralAction('Ambition', 'seeks station above his competence', INTENTIONAL_INTERIOR_EVIL,FORTITUDE))
        self.actions.append(moralAction('Inane Glory', 'seeks honour for his immorality ', INTENTIONAL_INTERIOR_EVIL, FORTITUDE))
        self.actions.append(moralAction('Pusilanimity', 'does the bare minimum', INTENTIONAL_INTERIOR_EVIL, FORTITUDE))
        self.actions.append(moralAction('Parvificence', 'acts miserly', INTENTIONAL_INTERIOR_EVIL,FORTITUDE))
        self.actions.append(moralAction('Effeminacy', 'does nothing but indulges his desires ', INTENTIONAL_INTERIOR_EVIL, FORTITUDE))
        self.actions.append(moralAction('Pertinacity', 'sticks to beliefs he knows are false', INTENTIONAL_INTERIOR_EVIL, FORTITUDE))

        #TEMPERANCE

        #POSITIVE
        self.actions.append(moralAction('Shame', 'realises his lowliness', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Honestia', 'prays for virtue', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Abstinence', 'gives up a pleasure for the sake of virtue', INTENTIONAL_INTERIOR_GOOD,TEMPERANCE))
        self.actions.append(moralAction('Fasting', 'fasts routinely', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Sobriety', 'does not get drunk for the whole year' , INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Continence', 'resolutely ignores temptation to evil', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Chastity', 'disciplines his carnality', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Clemency', ',in spite of being wronged, has mercy on ', INTENTIONAL_EXTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Modesty', 'acts so as not to provoke others to sin', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Humility', 'accepts a difficult truth and lives by it', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Eutrapelia', 'becomes good at reading', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Sportsmanship', 'becomes good at sport', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Decorum', 'disciplines his manners', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Silence', 'learns to not speak when unnecessary', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Studiousity', 'studies and passes an exam', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))
        self.actions.append(moralAction('Simplicity', 'clears out all unnecessary possessions', INTENTIONAL_INTERIOR_GOOD, TEMPERANCE))

        #NEGATIVE
        self.actions.append(moralAction('Gluttony', 'excessively eats', INTENTIONAL_INTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Drunkenness', 'becomes an alcoholic', INTENTIONAL_INTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Lust', 'loses discipline over his loins', INTENTIONAL_INTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Fornication', 'is adulterous with ', FORNICATION, TEMPERANCE))
        self.actions.append(moralAction('Adultery', 'cheats with ', FORNICATION, TEMPERANCE))
        self.actions.append(moralAction('Incontinence', 'lets his appetites dominate him', INTENTIONAL_INTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Anger', 'attacks ', VIOLENCE, TEMPERANCE))
        self.actions.append(moralAction('Cruelty', 'bullies ', VIOLENCE, TEMPERANCE))
        self.actions.append(moralAction('Pride', 'meditates on their own greatness', INTENTIONAL_INTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Curiousity', 'becomes overly interested in the private life of ', INTENTIONAL_EXTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Crudity', 'is intentionally rude to ', INTENTIONAL_EXTERIOR_EVIL, TEMPERANCE))
        self.actions.append(moralAction('Immodesty', 'acts out to get attention', INTENTIONAL_INTERIOR_EVIL, TEMPERANCE))

        #FAITH
        self.actions.append(moralAction('Prayer', 'prays without ceasing', INTENTIONAL_INTERIOR_GOOD, FAITH))
        self.actions.append(moralAction('Pilgrimage', 'goes on a pilgrimage', INTENTIONAL_INTERIOR_GOOD, FAITH))
        self.actions.append(moralAction('Vision', 'has a vision', INTENTIONAL_INTERIOR_GOOD, FAITH))

        self.actions.append(moralAction('Infidelity', 'refuses to believe the natural moral law', INTENTIONAL_INTERIOR_EVIL, FAITH))
        self.actions.append(moralAction('Heresy', 'denies parts of the moral law', INTENTIONAL_INTERIOR_EVIL, FAITH))
        self.actions.append(moralAction('Apostasy', 'denies God', INTENTIONAL_INTERIOR_EVIL, FAITH))
        self.actions.append(moralAction('Blasphemy', 'mocks God', INTENTIONAL_INTERIOR_EVIL, FAITH))

        #HOPE

        self.actions.append(moralAction('Read', 'reads Scripture', INTENTIONAL_INTERIOR_GOOD, HOPE))
        self.actions.append(moralAction('Despairs', 'despairs at salvation', INTENTIONAL_INTERIOR_EVIL, HOPE))
        self.actions.append(moralAction('Blasphemy', 'assumes salvation', INTENTIONAL_INTERIOR_EVIL, HOPE))

        #CHARITY
        self.actions.append(moralAction('Uncreated Light', 'experiences the uncreated light', INTENTIONAL_INTERIOR_GOOD, CHARITY))
        self.actions.append(moralAction('CharityVision', 'has a vision', INTENTIONAL_INTERIOR_GOOD, CHARITY))

        self.actions.append(moralAction('Hatred of God', 'begins to hate God', INTENTIONAL_INTERIOR_EVIL, CHARITY))
        self.actions.append(moralAction('Sloth', 'stops practicing his devotion', INTENTIONAL_INTERIOR_EVIL, CHARITY))
        self.actions.append(moralAction('Envy', 'intentionally teaches errors to ', INTENTIONAL_EXTERIOR_EVIL,CHARITY))
        self.actions.append(moralAction('Contention', 'argues with ', INTENTIONAL_EXTERIOR_EVIL, CHARITY))
        self.actions.append(moralAction('Schism', 'splits from the community', INTENTIONAL_INTERIOR_EVIL, CHARITY))
        self.actions.append(moralAction('Scandal', 'intentionally provokes ', INTENTIONAL_EXTERIOR_EVIL, CHARITY))

    def year(self, persons, year, markov):
         self.age += 1
         if self.sinCount > self.sinLimit:
             if self.isAlive:
                self.life = self.life + "Aged " + str(self.age) + " God loses patience with " + self.name + " "
                self.isAlive = False
                self.death()
                return
         if self.age > self.ageLimit:
             if self.isAlive:
                self.life = self.life + "Aged " + str(self.age) + " "
                self.isAlive = False
                self.death()
                return
             else:
                 return
         if self.virtue.inSin == True and (random.randrange(0, 2) == 1 or self.virtue.selectedVirtue == JUSTICE or self.virtue.selectedVirtue == CHARITY):
             self.life = self.life + "In year " + str(year) + ", " + self.name + repentence[random.randrange(0, 5)] + ":\n" + self.sinList
             self.sinList = ""
             self.virtue.inSin = False
         while 1:
             actionSelector = random.randrange(0, len(self.actions))
             if(self.actions[actionSelector].virtueOperatedOn == self.virtue.selectedVirtue and (self.actions[actionSelector].kindOfAction == INTENTIONAL_EXTERIOR_GOOD
             or self.actions[actionSelector].kindOfAction == INTENTIONAL_INTERIOR_GOOD) or self.actions[actionSelector].kindOfAction == THANKSGIVING):
                 if random.randrange(0,3) == 0:
                     self.life = self.life + intention[random.randrange(0, 5)]
                 self.doAction(self.actions[actionSelector], persons, markov, year)
                 break
         temptationType = random.randrange(0, 7) #One of the 7 Virtues will potentially be tested
         consentsToTemptation = random.randrange(0,10)
         self.temptation(persons, markov, year, temptationType, consentsToTemptation)
         '''
         action = self.actions[random.randrange(0, len(self.actions))]
 
  
          '''
    def temptation(self, persons, markov, year, temptationType, temptationTest):
        while 1:
            actionSelector = random.randrange(0, len(self.actions))
            if (self.actions[actionSelector].virtueOperatedOn == temptationType):
                finalTemptationScore = 150
                if temptationTest == FORTITUDE:
                    finalTemptationScore = temptationTest + self.virtue.fortitude
                elif temptationTest == JUSTICE:
                    finalTemptationScore = temptationTest + self.virtue.justice
                elif temptationTest == TEMPERANCE:
                    finalTemptationScore = temptationTest + self.virtue.temperance
                elif temptationTest == PRUDENCE:
                    finalTemptationScore = temptationTest + self.virtue.prudence
                elif temptationTest == FAITH:
                    finalTemptationScore = temptationTest + self.virtue.faith
                elif temptationTest == HOPE:
                    finalTemptationScore = temptationTest + self.virtue.hope
                elif temptationTest == CHARITY:
                    finalTemptationScore = temptationTest + self.virtue.charity
                if finalTemptationScore > 4: #With no virtue, there will be a lot of sinning
                    self.life = self.life + tempted[random.randrange(0,5)]
                    self.doAction(self.actions[actionSelector], persons, markov, year)
                break

    def doAction(self, action, persons, markov, year):
         if action.kindOfAction == INTENTIONAL_INTERIOR_EVIL:
             self.life = self.life + "In year " + str(year) + ", "
             self.interior_evil(action)
         elif action.kindOfAction == INTENTIONAL_INTERIOR_GOOD:
             self.life = self.life + "In year " + str(year) + ", "
             self.interior_good(action)
         elif action.kindOfAction == INTENTIONAL_EXTERIOR_GOOD or action.kindOfAction == THANKSGIVING:
             self.life = self.life + "In year " + str(year) + ", "
             self.exterior_good(action, persons[random.randrange(0, len(persons))])
         elif action.kindOfAction == INTENTIONAL_EXTERIOR_EVIL or action.kindOfAction == DECEPTION or action.kindOfAction == STEALING:
             self.life = self.life + "In year " + str(year) + ", "
             self.exterior_evil(action, persons[random.randrange(0, len(persons))])
         elif action.kindOfAction == VIOLENCE:
             self.life = self.life + "In year " + str(year) + ", "
             self.violence(action, persons[random.randrange(0, len(persons))], persons)
         elif action.kindOfAction == FORNICATION:
             self.life = self.life + "In year " + str(year) + ", "
             self.fornication(action, persons[random.randrange(0, len(persons))], persons, markov)
         elif action.kindOfAction == REPENTENCE:
             self.life = self.life + "In year " + str(year) + ", " + self.name + repentence[random.randrange(0,5)] + ":\n" + self.sinList
             self.sinList = ""
             self.virtue.inSin = False
    def interior_evil(self, action):
        virtueAttacked = action.virtueOperatedOn
        self.sinCount += 1
        self.virtue.inSin = True
        sentence = action.verb
        self.sinList = self.sinList + "Sins against "
        self.life = self.life + self.name + ' ' + sentence + '\n'

        if virtueAttacked == FORTITUDE:
            self.virtue.fortitude -= 1
            self.sinList = self.sinList + "Fortitude"
        elif virtueAttacked == HOPE:
            self.virtue.hope -= 1
            self.sinList = self.sinList + "Hope"
        elif virtueAttacked == FAITH:
            self.virtue.faith -= 1
            self.sinList = self.sinList + "Faith"
        elif virtueAttacked == CHARITY:
            self.sinList = self.sinList + "Charity"
            self.virtue.charity -= 1
        elif virtueAttacked == TEMPERANCE:
            self.sinList = self.sinList + "Temperance"
            self.virtue.temperance -= 1
        elif virtueAttacked == JUSTICE:
            self.sinList = self.sinList + "Justice"
            self.virtue.justice -= 1
        elif virtueAttacked == PRUDENCE:
            self.sinList = self.sinList + "Prudence"
            self.virtue.prudence -= 1
        self.sinList += "\n"
    def interior_good(self, action):
        virtueAttacked = action.virtueOperatedOn
        sentence = action.verb
        self.life = self.life + self.name + ' ' + sentence + '\n'

        if virtueAttacked == FORTITUDE:
            self.virtue.fortitude += 1
        elif virtueAttacked == HOPE:
            self.virtue.hope += 1
        elif virtueAttacked == FAITH:
            self.virtue.faith += 1
        elif virtueAttacked == CHARITY:
            self.virtue.charity += 1
        elif virtueAttacked == TEMPERANCE:
            self.virtue.temperance += 1
        elif virtueAttacked == JUSTICE:
            self.virtue.justice += 1
        elif virtueAttacked == PRUDENCE:
            self.virtue.prudence += 1

    def exterior_good(self, action, person):
        virtueAttacked = action.virtueOperatedOn
        sentence = action.verb
        self.life = self.life + self.name + ' ' + sentence + person.name + '\n'

        if virtueAttacked == FORTITUDE:
            self.virtue.fortitude += 1
            person.virtue.fortitude += 1
        elif virtueAttacked == HOPE:
            self.virtue.hope += 1
            person.virtue.hope += 1
        elif virtueAttacked == FAITH:
            self.virtue.faith += 1
            person.virtue.faith += 1
        elif virtueAttacked == CHARITY:
            self.virtue.charity += 1
            person.virtue.charity += 1
        elif virtueAttacked == TEMPERANCE:
            self.virtue.temperance += 1
            person.virtue.temperance += 1
        elif virtueAttacked == JUSTICE:
            self.virtue.justice += 1
            person.virtue.justice += 1
        elif virtueAttacked == PRUDENCE:
            self.virtue.prudence += 1
            person.virtue.prudence += 1

    def violence(self, action, person, personList):
        #virtueAttacked = action.virtueOperatedOn
        self.sinCount += 1
        sentence = action.verb
        self.virtue.inSin = True
        self.life = self.life + self.name + ' ' + sentence + person.name + '\n'
        self.sinList = self.sinList + "Murdering " + person.name + '\n'
        person.isAlive = False
        person.life += "Aged " + str(person.age) + " " + person.name + " is killed by " + self.name + "\n"
        person.death();
        personList.remove(person)
        self.virtue.charity = 0
        self.virtue.faith = 0
        self.virtue.hope = 0

    def exterior_evil(self, action, person):
        virtueAttacked = action.virtueOperatedOn
        sentence = action.verb
        self.sinList = self.sinList + "Sinning against " + person.name + '\n'
        self.virtue.inSin = True
        self.life = self.life + self.name + ' ' + sentence + person.name + '\n'
        self.sinCount += 1
        if virtueAttacked == FORTITUDE:
            self.virtue.fortitude -= 1
            person.virtue.fortitude -= 1
        elif virtueAttacked == HOPE:
            self.virtue.hope -= 1
            person.virtue.hope -= 1
        elif virtueAttacked == FAITH:
            self.virtue.faith -= 1
            person.virtue.faith -= 1
        elif virtueAttacked == CHARITY:
            self.virtue.charity -= 1
            person.virtue.charity -= 1
        elif virtueAttacked == TEMPERANCE:
            self.virtue.temperance -= 1
            person.virtue.temperance -= 1
        elif virtueAttacked == JUSTICE:
            self.virtue.justice -= 1
            person.virtue.justice -= 1
        elif virtueAttacked == PRUDENCE:
            self.virtue.prudence -= 1
            person.virtue.prudence -= 1

    def fornication(self, action, actedOn, personList, markov):
        virtueAttacked = action.virtueOperatedOn
        sentence = action.verb
        self.virtue.inSin = True
        self.life = self.life + self.name + ' ' + sentence + actedOn.name + '\n'
        self.sinList = self.sinList + "Relations with " + actedOn.name + '\n'
        personList.append(person(markov.New(), 0, markov, True, self))
        self.life = self.life + self.name + " begets " + personList[len(personList) - 1].name + '\n'
        personList[len(personList) - 1].generateActions()
        if virtueAttacked == FORTITUDE:
            self.virtue.fortitude -= 1
            actedOn.virtue.fortitude -= 1
        elif virtueAttacked == HOPE:
            self.virtue.hope -= 1
            actedOn.virtue.hope -= 1
        elif virtueAttacked == FAITH:
            self.virtue.faith -= 1
            actedOn.virtue.faith -= 1
        elif virtueAttacked == CHARITY:
            self.virtue.charity -= 1
            actedOn.virtue.charity -= 1
        elif virtueAttacked == TEMPERANCE:
            self.virtue.temperance -= 1
            actedOn.virtue.temperance -= 1
        elif virtueAttacked == JUSTICE:
            actedOn.virtue.justice -= 1
            person.virtue.justice -= 1
        elif virtueAttacked == PRUDENCE:
            actedOn.virtue.prudence -= 1
            person.virtue.prudence -= 1
