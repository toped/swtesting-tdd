"""
Assignment 4: Test Driven Development and Unit Testing

Objective:
Use test driven development to implement a set of software requirements. Write unit tests to provide full
coverage of developed code base using multi faceted independent tests. Create a control flow graph. Groups up
to 6.

Authors:
Tope Daramola
Hannah Church
Dylan Jaye
Mauri Mitchell

Python v2.7

"""
import math
import re  # import for regular expression module


# This function prints the user menu
def printMenu():
    print ("""
        1. Calculate Body Mass Index
        2. Find out if I can meet my savings goal
        3. Find the distance between two points
        4. Verify if my email address is valid
        """)


def calculateBMI(heightFeet, heightInches, weight):
    if (isinstance(heightFeet, int) or isinstance(heightFeet, float)) and (isinstance(heightInches, int) or isinstance(heightInches, float)) and (isinstance(weight, int) or isinstance(weight, float)):
        kgWeight = weight * 0.45
        totalHeightInches = (heightFeet * 12) + heightInches
        metricHeight = totalHeightInches * 0.025
        BMIValue = kgWeight / (math.pow(metricHeight, 2))
    else:
        message = "Please enter numeric values."
        return message
        
    if (BMIValue <= 18.5):
        message = "Your body mass index is: " + str(BMIValue) + ". You are underweight."
    elif(BMIValue > 18.5 and BMIValue < 25):
        message = "Your body mass index is: " + str(BMIValue) + ". You are of normal weight."
    elif (BMIValue >= 25 and BMIValue < 30):
        message = "Your body mass index is: " + str(BMIValue) + ". You are overweight."
    elif (BMIValue >= 30):
        message = "Your body mass index is: " + str(BMIValue) + ". You are obese."

    return message        

def calculateRetirement(age, salary, percentSaved, savingsGoal):
    if not isinstance(age, int) or not isinstance(salary, int) or not isinstance(percentSaved, int) or not isinstance(
            savingsGoal, int):
        result = "You must enter an integer, not a string"
        return result
    
    savedAnnually = salary * (percentSaved/100)
    amountAccrued = 0
    yearsSaved = 0

    if age >= 100:
        result = "The age you entered is too high.  You shouldn't be working!"
        return result

    while amountAccrued != savingsGoal:
        amountAccrued += savedAnnually
        yearsSaved += 1

    retirementAge = age + yearsSaved

    if retirementAge >= 100:
        result = "You will not meet your savings goal"
    else:
        result = retirementAge
        print("\n You can retire at " + str(retirementAge))

    return result

def calculateDistance(x1, y1, x2,y2):
    print("\n TO-DO: complete function")

def verifyEmailAddress(inputEmail):
    numAtSymbols = inputEmail.count('@')

    matchObject = re.search('^.+@.+\.[A-za-z]{1,2}$',
                  inputEmail)

    if matchObject and numAtSymbols == 1:
        return True
    else:
        return False

# Print the Menu
printMenu()

# Prompt user for the function that they want to run
funcType = 1 # input("What would you like to calculate? ")

if funcType == "1":
    print("\n BMI Calculator")
    #heightFeet = input("Enter the 'feet' dimension of your height: ")
    #heightInches = input("Enter the 'inches' dimension of your height: ")
    #weight = input("Enter your weight in pounds: ")
    #result = calculateBMI(heightFeet, heightInches, weight)
    #print(result)
elif funcType == "2":
    print("\n Savings Goal Calculator")
    # age = int(input("What is your current age? \n"))
    # salary = int(input("What is your current salary? \n"))
    # percentSaved = int(input("What percentage of your salary is saved each year? \n"))
    # savingsGoal = int(input("What is your savings goal? \n"))
    # print(calculateRetirement(age, salary, percentSaved, savingsGoal))

elif funcType == "3":
    print("\n Distance Calculator")
    print("\n TO-DO: prompt for user input then call function to return output")
elif funcType == "4":
    print("\n Email Verifier")
    inputString = 'hds109@msstate.ed'  # raw_input("Please enter an email address that you would like to verify: ")
    isValid = verifyEmailAddress(inputString)

    if isValid:
        print('\n Nice! The email you provided is valid')
    else:
        print('\n Sorry. The email you provided is invalid')

