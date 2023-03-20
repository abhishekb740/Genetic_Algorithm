import random

def fitnessFunction(population) -> list:
    populationSize = len(population)
    xValues = []
    for i in range (populationSize):
        value = 0.0
        for j in range (5):
            value = 2*value + population[i][j]
        xValues.append(value)
    fxValues = []
    for i in range (populationSize):
        fxValues.append(xValues[i]**2)
    avgValue = 0.0
    for i in range (populationSize):
        avgValue += fxValues[i]
    avgValue = avgValue/populationSize
    expectedCount = []
    for i in range (populationSize):
        expectedCount.append(fxValues[i]/avgValue)
    actualCount = []
    for i in range (populationSize):
        actualCount.append(round(expectedCount[i]))
    parentalChromosomes = []
    for i in range (populationSize):
        for j in range (actualCount[i]):
            parentalChromosomes.append(population[i])
    return parentalChromosomes

def onePointCrossoverFunction(parentalChromosomes, crossoverPoint, parentalChromosomeSize) -> list:
    random.shuffle(parentalChromosomes)
    offSpring = []
    for i in range(int(parentalChromosomeSize/2)):
        child1 = parentalChromosomes[(2*i)][0:crossoverPoint]
        child2 = parentalChromosomes[(2*i)+1][crossoverPoint:6]
        offSpring.append(child1+child2)
        child3 = parentalChromosomes[(2*i)+1][0:crossoverPoint]
        child4 = parentalChromosomes[(2*i)][crossoverPoint:6]
        offSpring.append(child3+child4)
    return offSpring

def twoPointCrossOverFunction(parentalChromosomes, crossoverPoint1, crossoverPoint2, parentalChromosomeSize) -> list:
    random.shuffle(parentalChromosomes)
    offSpring = []
    for i in range(int((parentalChromosomeSize/2))):
        child1 = parentalChromosomes[2*i][0:crossoverPoint1]
        child2 = parentalChromosomes[(2*i)+1][crossoverPoint1:crossoverPoint2]
        child3 = parentalChromosomes[2*i][crossoverPoint2:6]
        offSpring.append(child1+child2+child3)
        child4 = parentalChromosomes[(2*i)+1][0:crossoverPoint1]
        child5 = parentalChromosomes[2*i][crossoverPoint1:crossoverPoint2]
        child6 = parentalChromosomes[(2*i)+1][crossoverPoint2:6]
        offSpring.append(child4+child5+child6)
    return offSpring

def bitFlipFunction(offSpring, bitNumberFlipped) -> list:
    offSpringSize = len(offSpring)
    for i in range(offSpringSize):
        if(offSpring[i][4] == 0):
            offSpring[i][4] = 1
        elif(offSpring[i][4] == 1):
            offSpring[i][4] = 0
    return offSpring

def swapMutationFunction(offSpring, bit1ToBeFlipped, bit2ToBeFlipped) -> list:
    offSpringSize = len(offSpring)
    for i in range(offSpringSize):
        offSpring[i][bit1ToBeFlipped], offSpring[i][bit2ToBeFlipped] = offSpring[i][bit2ToBeFlipped], offSpring[i][bit1ToBeFlipped]
    return offSpring

def maximumUtiliyFunction(offSpring) -> int:
    offSpringSize = len(offSpring)
    maximumValue = 0.0
    for i in range (offSpringSize):
        value = 0.0
        for j in range (5):
            value = value*2 + offSpring[i][j]
        if(value>maximumValue):
            maximumValue = value
    return maximumValue

def geneticAlgorithmFunction():
    populationSize = int(input("Please Enter your Population Size: "))
    if populationSize==1:
        print("You cannot give Population Size as 1, Enter the Value greater than 1!")
        return
    population = [[random.randint(0,1) for i in range(5)] for i in range(populationSize)]
    # population = [[1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [1, 1, 0, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0]]
    crossoverTypeC = int(input("Please Enter 0 for One Point Crossover or 1 for Two Point Crossover: "))

    if not crossoverTypeC == 0 and not crossoverTypeC == 1:
        print("Warning: Please Enter the Valid Input as per the Instruction")
        return

    mutationTypeM = int(input("Please Enter 0 for Bit Swap or 1 for swap mutation: "))
    if not mutationTypeM == 0 and not mutationTypeM == 1:
        print("Warning: Please Enter the Valid Input as per the Instruction")
        return

    terminationConditionT = int(input("Please Enter 0 for default Termination(No Improvement) or 1 for Predefined Iteration: "))
    if terminationConditionT != 0 and terminationConditionT != 1:
        print("Warning: Please Enter the Valid Input as per the Instruction")
        return
    
    i = 0.0
    x = 0.0
    maximum = 0.0
    if terminationConditionT == 0:
        x = int(input("Please Enter the value of x: "))
    elif terminationConditionT==1:
        i = int(input("Please Enter the value of i: "))


    if terminationConditionT == 1:
        for i in range (i):
            parentalChromosomes = fitnessFunction(population) 
            parentalChromosomesSize = len(parentalChromosomes)

            if crossoverTypeC == 0:
                offSpring = twoPointCrossOverFunction(parentalChromosomes, 1, 3, parentalChromosomesSize)
            elif crossoverTypeC == 1:
                offSpring = onePointCrossoverFunction(parentalChromosomes, 2, parentalChromosomesSize)
            if mutationTypeM == 0:
                offSpring = bitFlipFunction(offSpring, 4)
            elif mutationTypeM == 1:
                offSpring = swapMutationFunction(offSpring, 1, 3)
            maximum = maximumUtiliyFunction(offSpring)
            population = offSpring
    elif terminationConditionT == 0:
        count = 0.0
        while(count!=x):
            parentalChromosomes = fitnessFunction(population) 
            parentalChromosomesSize = len(parentalChromosomes)

            if crossoverTypeC == 0:
                offSpring = twoPointCrossOverFunction(parentalChromosomes, 1, 3, parentalChromosomesSize)
            elif crossoverTypeC == 1:
                offSpring = onePointCrossoverFunction(parentalChromosomes, 2, parentalChromosomesSize)
            
            if mutationTypeM == 0:
                offSpring = bitFlipFunction(offSpring, 4)
            elif mutationTypeM == 1:
                offSpring = swapMutationFunction(offSpring, 1, 3)

            population = offSpring
            if maximum < maximumUtiliyFunction(offSpring):
                count = 0
                maximum = maximumUtiliyFunction(offSpring)
            elif maximum >= maximumUtiliyFunction(offSpring):
                count += 1

    print(maximum)

geneticAlgorithmFunction()