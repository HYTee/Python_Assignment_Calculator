#  Resistor Calculator
#  Date      Author          Info
#  6/4/21    Iza Norshahril  1st Build 
# 29/4/21    HY Tee          2nd Build with succeed connection to VBA through Batch
import sys
def getInput():
    y = ""
    if (len(sys.argv)-1) == 4 :
        y = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4]
    elif (len(sys.argv)-1) == 5 :
        y = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5]
    elif (len(sys.argv)-1) == 6 :
        y = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6]
    
    userInput = [x for x in y.split(" ")] #takes all input then split by each space
    userInput = [x.lower() for x in userInput] #to make all lower case so it''ll be easy to compare later
    #print(userInput) # check userInput
    return userInput

def erroroutput(numberseq,code):
    print("\nInvalid {} color input! Please enter the colors in the list below only. Thanks".format(numberseq))
    print(code)
    userInput = checkInput(getInput())
    return userInput

def checkInput(userInput):
#    for x in userInput:
#        if x not in colors:
#            print("\nInvalid input! Please enter the colors in the list below only. Thanks")
#            print(colors)
#            userInput = checkInput(getInput())
#           break
    if(len(userInput) < 4):
        print("\nLess than 4 inputs, let's try again :)")
        userInput = checkInput(getInput())
    elif(len(userInput) > 6):
        # print("\nMore than 6 inputs...calculate the 1st six only :) ")
        # userInput = userInput[:6]
        print("\nMore than 6 inputs, please check again :)")
        userInput = checkInput(getInput())  
        
    elif(len(userInput) == 4):
        if userInput[0] not in num_code.keys():
            userInput = erroroutput("1st",list(num_code.keys()))
            
        elif userInput[1] not in num_code.keys():
            userInput = erroroutput("2nd",list(num_code.keys()))
            
        elif userInput[2] not in multiplier.keys():
            userInput = erroroutput("3rd",list(multiplier.keys()))
            
        elif userInput[3] not in tolerance.keys():
            userInput = erroroutput("4th",list(tolerance.keys()))
    
    elif(len(userInput) == 5) or (len(userInput) == 6):
           
        if userInput[0] not in num_code.keys():
            userInput = erroroutput("1st",list(num_code.keys()))
            
        elif userInput[1] not in num_code.keys():
            userInput = erroroutput("2nd",list(num_code.keys()))
            
        elif userInput[2] not in num_code.keys():
            userInput = erroroutput("3rd",list(num_code.keys()))
            
        elif userInput[3] not in multiplier.keys():
            userInput = erroroutput("4th",list(multiplier.keys()))
            
        elif userInput[4] not in tolerance.keys():
            userInput = erroroutput("5th",list(tolerance.keys()))
            
        if (len(userInput) == 6):
            if userInput[5] not in ppm.keys():
                userInput = erroroutput("6th",list(ppm.keys()))
                
    return userInput

def simplify_ans (Rvalue):
    if Rvalue >= 1000000000:
        ans = str(Rvalue/1000000000) + "G Ohm"
    elif 1000000 <= Rvalue <=1000000000:
        ans = str(Rvalue/1000000000) + "M Ohm"
    elif 1000 <= Rvalue <=1000000:
        ans = str(Rvalue/1000) + "k Ohm"
    elif 0 <= Rvalue <=1000:
        ans = str(Rvalue/1000) + "Ohm"
    return ans

#colors = [
#       'black',
#        'brown',
#        'red',
#        'orange',
#        'yellow',
#        'green',
#        'blue',
#        'violet',
#        'grey',
#        'white',
#       'gold',
#        'silver']
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
multiplier = {
        'black': '1',
        'brown': '10',
        'red': '100',
        'orange':'1000',
        'yellow':'10000',
        'green':'100000',
        'blue':'1000000',
        'violet':'10000000',
        'grey':'100000000',
        'white':'1000000000',
        'gold': '0.1',
        'silver': '0.01'
         }
tolerance = {
    'brown' : '+-1%',
    'red' : '+-2%',
    'green' : '+-0.5%',
    'blue' : '+-0.25%',
    'violet' : '+-0.1%',
    'grey' : '+-0.05%',
    'gold' : '+-5%',
    'silver' : '+-10%'
}

ppm = {
    'brown' : '100ppm',
    'red' : '50ppm',
    'orange' : '15ppm',
    'yellow' : '25ppm',
    'blue' : '10ppm',
    'violet' : '5ppm'
    }
run=1
while(run==1):
    #print ("######## Resistor Color Code Calculator #######")
    userInput = checkInput(getInput())

    if(len(userInput) == 4):
        x1 = int(num_code[userInput[0]])
        x2 = int(num_code[userInput[1]])
        x3 = float(multiplier[userInput[2]])
        x4 = tolerance[userInput[3]]
    
        Rvalue = ((x1*10)+x2)*x3
        ans = simplify_ans(Rvalue)
        sys.stdout.write("{} {}".format(ans,x4))
    
    elif(len(userInput) == 5):
        x1 = int(num_code[userInput[0]])
        x2 = int(num_code[userInput[1]])
        x3 = int(num_code[userInput[2]])
        x4 = float(multiplier[userInput[3]])
        x5 = tolerance[userInput[4]]
    
        Rvalue = ((x1*100)+(x2*10)+x3)*x4
        ans = simplify_ans(Rvalue)
        sys.stdout.write("{} {}".format(ans,x5))

    elif(len(userInput) == 6):
        x1 = int(num_code[userInput[0]])
        x2 = int(num_code[userInput[1]])
        x3 = int(num_code[userInput[2]])
        x4 = float(multiplier[userInput[3]])
        x5 = tolerance[userInput[4]]
        x6 = ppm[userInput[5]]
    
        Rvalue = ((x1*100)+(x2*10)+x3)*x4
        ans = simplify_ans(Rvalue)
        sys.stdout.write("{} {} {}".format(ans,x5,x6))
    
    run=0
    #while(1):
    #    recalc = input("Do you want to calculate another resistor value? (y/n) : ")
    #    if(recalc == 'y'):
    #        run=1
    #        print("\n")
    #        break
    #    if(recalc == 'n'):
    #        print("\nByeBye.Thank you.")
    #        break
    #    else:
    #        print("\nInvalid Input\n")
           
