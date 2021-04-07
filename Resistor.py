# Resistor Calculator
# Date      Author          Info
# 6/4/21    Iza Norshahril  1st Build 

def getInput():
    userInput = [x for x in input("\nPlease input each band's color separated by space : ").split(" ")] #takes all input then split by each space
    userInput = [x.lower() for x in userInput] #to make all lower case so it''ll be easy to compare later
    #print(userInput) # check userInput
    return userInput

def checkInput(userInput):
    for x in userInput:
        if x not in colors:
            print("\nInvalid input! Please enter the colors in the list below only. Thanks")
            print(colors)
            userInput = checkInput(getInput())
            break
    if(len(userInput) < 4):
        print("\nLess than 4 inputs, let's try again :)")
        userInput = checkInput(getInput())
    elif(len(userInput) > 6):
        # print("\nMore than 6 inputs...calculate the 1st six only :) ")
        # userInput = userInput[:6]
        print("\nMore than 6 inputs, please check again :)")
        userInput = checkInput(getInput())  
    return userInput

colors = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white',
        'gold',
        'silver']
num_code = {
        'black': '0',
        'brown': '1',
        'red': '2',
        'orange':'3',
        'yellow':'4',
        'green':'5',
        'blue':'6',
        'violet':'7',
        'grey':'8',
        'white':'9'
        }
print ("######## Resistor Color Code Calculator #######")
userInput = checkInput(getInput())
print(userInput)
print(num_code)
