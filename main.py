from person import person
import random
from Markov import Markov
print('Test')

personList = []
numberOfPeople = 20
people = 0
year = 1


babylonian = Markov('babylonian.txt')
latin = Markov('latin.txt')
hebrew = Markov('hebrew.txt')
greek = Markov('greek.txt')
egyptian = Markov('egyptian.txt')

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

people = 0
while people < numberOfPeople:
    #print(personList[people].life)
    personList[people].death()
    people += 1

print("The main character is " + personList[0].name)