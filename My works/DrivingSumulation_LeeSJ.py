import random
import math

print "==================================================================="
print "############### Welcome to the Driving Simulation #################"
print "==================================================================="
print ""
print ""
print "==============================="
print ""
print "1. Hope, BC, Canada"
print "2. Las Vegas, Nevada, US"
print "3. Hong Kong, China"

Answer1 = int(raw_input("Choose a city you want to drive (1~3): "))

print "==============================="
print ""
print "1. 2021 Honda Civic Sedan"
print "2. 2019 BMW 330i"
print "3. 2019 Ferrari 812 Superfast"
Answer2 = int(raw_input("Choose a car you want to drive (1~3): "))

print "==============================="
print "1. Flat road"
print "2. Bumpy road"
print "3. Muddy road"
Answer3 = int(raw_input("Choose a road condition (1~3): "))

print "==============================="
print "1. Sunny"
print "2. Rainy"
print "3. Snowy"
Answer4 = int(raw_input("Choose a weather condition (1~3): "))

if Answer2 ==3:
    print "==============================="
    print "1. 1"
    print "2. 2"
    Answer5 = int(raw_input("Choose the number of people in your car including you (1~2): "))
else:
    print "==============================="
    print "1. 1"
    print "2. 2"
    print "3. 3"
    print "4. 4"
    print "5. 5"
    Answer5 = int(raw_input("Choose the number of people in your car including you (1~5): "))

print "==============================="
print "1. morning"
print "2. afternoon"
print "3. evening"
print "4. late night"
Answer6 = int(raw_input("Choose a time you will drive (1~4): "))

print "==============================="
print "1. weekday"
print "2. weekend"
Answer7 = int(raw_input("Choose a day you will drive (1~2): "))

print "==============================="
print "1. Yes"
print "2. No"
Answer8 = int(raw_input("Choose if there is a special event on that day (1~2): "))

print "==============================="
Answer9 = int(raw_input("How many miles you want to drive? \n@@@@@ 5~50 is recommended.@@@@@ \n @@@@@If you put a number higher than 100, it will take too much time @@@@@: "))

detailCar = ["4 cyl, 1.5L, Automatic, Regular Gasoline, Turbo, SIDI, 5 seats, 33.0MPG", 
             "4 cyl, 2.0L, Automatic (S8), Premium Gasoline, Turbo, SIDI, 5 seats, 30.0MPG",
             "12 cyl, 6.5L, Automatic (AM7), Premium Gasoline, SIDI, 2 seats, 13.0MPG"]

population = [6181, 635000, 7500000]
area = [41, 367, 1106]

city = ["Hope, BC, Canada", "Las Vegas, Nevada, US", "Hong Kong, China"]
car = ["2021 Honda Civic Sedan", "2019 BMW 330i", "2019 Ferrari 812 Superfast"]
roadCondition = ["Flat road","Bumpy road","Muddy road"]
weather = ["Sunny","Rainy","Snowy"]
numPeople = ["1", "2", "3", "4", "5"]
time = ["morning","afternoon","evening", "late night"]
day = ["weekday","weekend"]
event = ["yes","no"]

def Summary():
        print "City:",city[Answer1-1]
        print "Detailed city info: "
        print "       Population:", population[Answer1-1]
        print "       Area:", area[Answer1-1], "km^2"
        print "Car:", car[Answer2-1]
        print "Detailed car info: "
        print "       ", detailCar[Answer2-1]
        print "Road Condition:", roadCondition[Answer3-1]
        print "Weather:", weather[Answer4-1]
        print "Number of people in your car:", numPeople[Answer5-1]
        print "Time:", time[Answer6-1]
        print "Day:", day[Answer7-1]
        print "Special Event on the day:", event[Answer8-1]
        print "The distance you will drive:", Answer9, "miles"
        

print "==================================================================="
print "############### Here is a summary of your choice #################"
print ""
Summary()
print ""
print "##################################################################"
print "==================================================================="
print ""
print ""

Start = raw_input("Enter any characters or number to begin: ")
print "==================== Let's start a simulation ====================="

def milesPerLight():
    density = population[Answer1-1]/area[Answer1-1]
    isValue = round(5/(1.5*(1+round(8*(math.log10(density)-2)))),3)
    return isValue

isValue = milesPerLight()

#print "isValue:", isValue

MPGs = [33.0, 30.0, 13.0]
MPG = MPGs[Answer2-1]

print "original MPG:",MPG

def MPGcalculator(MPG):
    if Answer3 == 1:
        MPG *= 1
    elif Answer3 == 2:
        MPG *=0.95
    else:
        MPG *=0.9

    if Answer4 == 1:
        MPG *= 1
    elif Answer4 == 2:
        MPG *=0.95
    else:
        MPG *=0.85
    
    if Answer5 == 1:
        MPG *= 1
    elif Answer5 == 2:
        MPG *=0.93
    elif Answer5 == 3:
        MPG *=0.86
    elif Answer5 == 4:
        MPG *=0.79
    else:
        MPG *=0.72

    if Answer6 == 1:
        MPG *= 0.9
    elif Answer6 == 2:
        MPG *=0.75
    elif Answer6 == 3:
        MPG *= 0.83
    else:
        MPG *=1.0

    if Answer7 == 1:
        MPG *= 1.0
    else:
        MPG *=0.9

    if Answer8 == 1:
        MPG *= 0.8
    else:
        MPG *=1.0
    MPG = round(MPG,2)
    return MPG

MPG = MPGcalculator(MPG)

print "MPG after the selections applied:",MPG

gasConsumption = round(1/MPG,3)
print "gasConsumption:",gasConsumption

numGreen = 0
numYellow = 0
numRed = 0
distanceDriven = 0
gasConsumed = 0
totalGasConsumption = 0
totaldistanceDriven = 0

def green(distanceDriven):
    global gasConsumption
    print "Green light, Proceeded without stop"
    gasConsumed = round(distanceDriven*gasConsumption*1.0,3)
    return gasConsumed
    
def yellow(distanceDriven):
    global gasConsumption
    randomFactor = random.random()
    if randomFactor <0.5:
        print "Yellow light, Slowed down"
        gasConsumed = round(distanceDriven*gasConsumption*1.1,3)
        return gasConsumed
    else:
        print "Yellow light, Proceeded without slowing down"
        gasConsumed = round(distanceDriven*gasConsumption*1.0,3)
        return gasConsumed

def red(distanceDriven):
    global gasConsumption
    randomFactor = random.random()
    if randomFactor <0.7:
        print "Red light, Stopped"
        gasConsumed = round(distanceDriven*gasConsumption*1.2,3)
        return gasConsumed
    else:
        print "Stop sign, Stopped"
        gasConsumed = round(distanceDriven*gasConsumption*1.2,3)
        return gasConsumed 

def facedLight():
    print ""
    
    print ""
    print "Faced a light!"
    global numGreen
    global numYellow
    global numRed
    global distanceDriven
    global gasConsumed
    global totalGasConsumption
    global totaldistanceDriven
    global gasConsumption
    
    distanceDriven = round(isValue*(float(random.randint(70,130))/100),2)
    totaldistanceDriven += distanceDriven
    
    signal = random.randint(1,3)
    if signal == 1:
        numGreen += 1
        gasConsumed = green(distanceDriven)
    elif signal == 2:
        numYellow += 1
        gasConsumed = yellow(distanceDriven)
    else:
        numRed += 1
        gasConsumed = red(distanceDriven)
    
    return distanceDriven,totaldistanceDriven,numGreen,numYellow,numRed,gasConsumption

while totaldistanceDriven <=Answer9:
    print "---------------------------------------------"
    facedLight()
    
    randomFactor = random.random()
    
    if randomFactor <=0.33:
        print "it was not jammed"
    elif randomFactor >0.33 and randomFactor <=0.67:
        print "it was little jammed"
        gasConsumption *=1.1
        gasConsumed = round(distanceDriven*gasConsumption,3)
        gasConsumption /=1.1
    else:
        print "it was jammed"
        gasConsumption *=1.2
        gasConsumed = round(distanceDriven*gasConsumption,3)
        gasConsumption /=1.2

    print ""
    print "distanceDriven:",distanceDriven
    print "gasConsumed:",gasConsumed
    print ""
            
    print "---------------------------------------------"
    totalGasConsumption = round(totalGasConsumption+gasConsumed,3)

    print "Total distance drove:", totaldistanceDriven
    print "Total gas consumed:", totalGasConsumption

print "############################################################"
print "############# --Driving simulation is done-- ###############"
print "#####                                                  #####"
print "#####        Total number of green lights:", numGreen, "          #####"
print "#####        Total number of yellow lights:", numYellow, "         #####"
print "#####    Total number of red lights/stop signs:",numRed, "     #####"
print "#####                                                  #####"
print "#####        Total distance drove:", totaldistanceDriven, "miles        #####"
print "#####         Total gas consumed:", totalGasConsumption, "gallons        #####"
print "############################################################"
print "############################################################"
        
    
    
    
    
