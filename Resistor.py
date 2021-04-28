# Resistor Calculator
# Date      Author          Info
#  6/4/21   Iza Norshahril  1st Build 
# 28/4/21   Fikri           Calc & print function
# 28/4/21   Iza Norshahril  Put all def in class

class Resistor():
    def __init__(self):
        # print("Test")
        self.runAll()

    def erroroutput(self,numberseq,code):
        print("\nInvalid {} color input! Please enter the colors in the list below only. Thanks".format(numberseq))
        print(code)
        userInput = self.checkInput(self.getInput())
        return userInput

    def getInput(self):
        userInput = [x for x in input("\nPlease input each band's color separated by space : ").split(" ")] #takes all input then split by each space
        userInput = [x.lower() for x in userInput] #to make all lower case so it''ll be easy to compare later
        #print(userInput) # check userInput
        return userInput

    def checkInput(self,userInput):
    #    for x in userInput:
    #        if x not in colors:
    #            print("\nInvalid input! Please enter the colors in the list below only. Thanks")
    #            print(colors)
    #            userInput = checkInput(getInput())
    #           break
        wrongInput=1
        if(len(userInput) < 4):
            print("\nLess than 4 inputs, let's try again :)")
            
        elif(len(userInput) > 6):
            # print("\nMore than 6 inputs...calculate the 1st six only :) ")
            # userInput = userInput[:6]
            print("\nMore than 6 inputs, please check again :)")
            
        elif(len(userInput) in [4,5,6]):
            if userInput[0] not in self.num_code.keys():
                # print("\nInvalid 1st color input! Please enter the colors in the list below only. Thanks")
                # print(self.num_code.keys())
                userInput = self.erroroutput("1st",list(self.num_code.keys()))
                
            elif userInput[1] not in self.num_code.keys():
                # print("\nInvalid 2nd color input! Please enter the colors in the list below only. Thanks")
                # print(self.num_code.keys())
                userInput = self.erroroutput("2nd",list(self.num_code.keys()))
            
            if(len(userInput) == 4):
                if userInput[2] not in self.multiplier.keys():
                    # print("\nInvalid 3rd color input! Please enter the colors in the list below only. Thanks")
                    # print(self.multiplier.keys())
                    userInput = self.erroroutput("3rd",list(self.multiplier.keys()))
                    
                elif userInput[3] not in self.tolerance.keys():
                    # print("\nInvalid 4th color input! Please enter the colors in the list below only. Thanks")
                    # print(self.tolerance.keys())
                    userInput = self.erroroutput("4th",list(self.tolerance.keys()))
                # else:
                #     wrongInput=0
        
            if(len(userInput) in [5,6]):
                                
                if userInput[2] not in self.num_code.keys():
                    # print("\nInvalid 3rd color input! Please enter the colors in the list below only. Thanks")
                    # print(self.num_code.keys())
                    userInput = self.erroroutput("3rd",list(self.num_code.keys()))
                    
                elif userInput[3] not in self.multiplier.keys():
                    # print("\nInvalid 4th color input! Please enter the colors in the list below only. Thanks")
                    # print(self.multiplier.keys())
                    userInput = self.erroroutput("4th",list(self.multiplier.keys()))
                    
                elif userInput[4] not in self.tolerance.keys():
                    # print("\nInvalid 5th color input! Please enter the colors in the list below only. Thanks")
                    # print(self.tolerance.keys())
                    userInput = self.erroroutput("5th",list(self.tolerance.keys()))
                    
                if (len(userInput) == 6):
                    if userInput[5] not in self.ppm.keys():
                        # print("\nInvalid 6th color input! Please enter the colors in the list below only. Thanks")
                        # print(self.ppm.keys())
                        userInput = self.erroroutput("6th",list(self.ppm.keys()))
                # else:
                #     wrongInput=0
            
        # if(wrongInput):
        #     userInput = self.checkInput(self.getInput())
        return userInput

    def simplify_ans (self,Rvalue):
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
# run=1
# while(run==1):
    
    def printOutput(self):
        print ("######## Resistor Color Code Calculator #######")
        userInput = self.checkInput(self.getInput())

        if(len(userInput) == 4):
            x1 = int(self.num_code[userInput[0]])
            x2 = int(self.num_code[userInput[1]])
            x3 = float(self.multiplier[userInput[2]])
            x4 = self.tolerance[userInput[3]]
        
            Rvalue = ((x1*10)+x2)*x3
            ans = self.simplify_ans(Rvalue)
            print("The 4 Band Resistor value is {} {} \n".format(ans,x4))
        
        elif(len(userInput) == 5):
            x1 = int(self.num_code[userInput[0]])
            x2 = int(self.num_code[userInput[1]])
            x3 = int(self.num_code[userInput[2]])
            x4 = float(self.multiplier[userInput[3]])
            x5 = self.tolerance[userInput[4]]
        
            Rvalue = ((x1*100)+(x2*10)+x3)*x4
            ans = self.simplify_ans(Rvalue)
            print("The 5 Band Resistor value is {} {} \n".format(ans,x5))

        elif(len(userInput) == 6):
            x1 = int(self.num_code[userInput[0]])
            x2 = int(self.num_code[userInput[1]])
            x3 = int(self.num_code[userInput[2]])
            x4 = float(self.multiplier[userInput[3]])
            x5 = self.tolerance[userInput[4]]
            x6 = self.ppm[userInput[5]]
        
            Rvalue = ((x1*100)+(x2*10)+x3)*x4
            ans = self.simplify_ans(Rvalue)
            print("The 6 Band Resistor value is {} {} {} \n".format(ans,x5,x6))

    def runAll(self):
        run=1
        while(run):
            self.printOutput()
            while(run):
                recalc = input("Do you want to calculate another resistor value? (y/n) : ")
                if(recalc == 'y'):
                    print("\n")
                    break
                elif(recalc == 'n'):
                    print("\nByeBye.Thank you.")
                    run=0
                    break
                else:
                    print("\nInvalid Input\n")

Resistor() # call class
