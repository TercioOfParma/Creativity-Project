from person import person
import random
from Markov import Markov
from operator import itemgetter

personList = []
numberOfPeople = 500
generationNumber = 500
people = 0
year = 1
generations = 20
generationFactor = 5
babylonian = Markov('babylonian.txt')
latin = Markov('latin.txt')
hebrew = Markov('hebrew.txt')
greek = Markov('greek.txt')
egyptian = Markov('egyptian.txt')

def generateGeneration(tempList):
    personList = sorted(tempList, key=lambda current: current.score, reverse=True)
    toGet = int(generationNumber / generationFactor)
    i = 0
    newList = []
    print("Number Survived: " + str(numberOfPeople) + " toGet " + str(toGet))
    fashion = egyptian
    while i < generationNumber:
        choose = random.randrange(1, 5)
        if choose == 1:
            fashion = latin
        if choose == 2:
            fashion = hebrew
        if choose == 3:
            fashion = babylonian
        if choose == 4:
            fashion = greek
        if choose == 5:
            fashion = egyptian
        tempPerson = person(fashion.New(), random.randrange(0, 40), fashion, False) #New person named based on the times
        tempPerson.virtue.spliceCharacter(personList[random.randrange(0, toGet)], personList[random.randrange(0, toGet)])
        tempPerson.generateActions()
        newList.append(tempPerson)
        i += 1
    return newList

print(egyptian.New())
while people < numberOfPeople:
    choose = random.randrange(1, 5)
    name = ''
    markovChain = greek
    if choose == 1:
        name = latin.New()
        markovChain = latin
        print(name)
    if choose == 2:
        name = hebrew.New()
        markovChain = hebrew
    if choose == 3:
        name = babylonian.New()
        markovChain = babylonian
    if choose == 4:
        name = greek.New()
    if choose == 5:
        name = egyptian.New()
        markovChain = egyptian
    personList.append(person(name, random.randrange(0, 40), markovChain, False))
    personList[people].generateActions()
    people += 1
print(personList)
fashion = egyptian
i = 0
while i < generations:
    print("Generation " + str(i))
    while personList[0].isAlive:
        people = 0
        print("YEAR " + str(year))
        fashion = random.randrange(0,5)
        #Randomly varies out the names
        if fashion == 0:
            fashion = greek
        elif fashion == 1:
            fashion = latin
        elif fashion == 2:
            fashion = babylonian
        elif fashion == 3:
            fashion = hebrew
        elif fashion == 4:
            fashion = egyptian
        while people < numberOfPeople:
            if personList[people].isAlive:
                personList[people].year(personList, year, fashion)
            people += 1
            numberOfPeople = len(personList)
        year += 1
    year = 0
    i += 1
    people = 0

    while people < numberOfPeople:
        #print(personList[people].life)
        personList[people].death()
        people += 1

    if i != generations:
        personList = generateGeneration(personList)
        numberOfPeople = generationNumber


personList = sorted(personList, key=lambda current: current.score, reverse=True)

print("The main character is " + personList[0].name)
personList[0].outputLife() #The highest scored character in 150 generations