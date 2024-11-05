from datetime import datetime
import time
import sys


#Done by both students
def main():     #This function will ask the user to login or sign up. It is the the main function and the first function to be executed in the program.
    logOrSign = input("select either login (L) or sign up (S) > ")      #Asks the user wethere they wish to create a new account or login.
    validLogOrSign = False      #This is used in the while loop and can stop the loop when the condition changes.
    counterOfTransactions = 0   #This counter is used in the termination function to display the recent transactions during a session. it must always be initilized to zero when running the program
    while not validLogOrSign:   #This loop will keep asking the user to enter the correct input to signify whether the user wishes to sign up or login
        if logOrSign.upper() == "S" or logOrSign.upper == "SIGN UP" or logOrSign.upper == "SIGNUP":     #An if statement for signup
            validcreate = True      #This boolean value is to confirm the create function in order for the user to create a new account
            validLogOrSign= True    #if user chooses to sign up it will break the loop
            create(validcreate,counterOfTransactions)   #Calling this function will redirect the user to the create function where the user can create a new account. the counter is passed to all functions.
        elif logOrSign.upper() == "L" or logOrSign.upper == "LOGIN":    #An else if statement for login
            validLogin = True       #This boolean value is to confirm the login function in order for the user to login to their account
            validLogOrSign = True   #if user chooses to login it will break the loop
            login(validLogin,counterOfTransactions)     #Calling this function will redirect the user to the login function where the user can login to their account. the counter is passed to all functions.
        else:   #An else statement if the user enters an incorrect input
            logOrSign = input("Wrong input, Please select either login (L) or sign up (S) > ")     #Asks the user for the corrected input


#Done by both students
def create(validcreate,counterOfTransactions):      #This funtion is used to create a new account for the user

    #First part will ask for the card number#

    validCardNumber = False     #This is used in the while loop and can stop the loop when the condition changes just like (break).
    if validcreate == True:     #This is passed from the main funtion to fully confirm to the program that it can execute the create function
        while not validCardNumber:      #This loop will keep asking the user to enter a unique 4-digit card number 
            try:        #We use try incase of any possible errors in input, for example if the user enters only one digit.

                cardNumber = input("Enter unique 4-digit card number: ")    #Will ask the user for a unique 4-digit card number
                if cardNumber.isdigit():        #An if state to make sure that the string entered is only digit numbers

                    #These if statement will only run if the input was a digit number. It will make sure that the number enter is unique by comparing index values. the try will make sure the user enters 4 digit numbers
                    if cardNumber[0] == cardNumber[1]:      
                        validCard = False    #If the entered digit number is not fully unique it will set this to a boolean variable false
                    elif cardNumber[0] == cardNumber[2]: 
                        validCard = False    
                    elif cardNumber[0] == cardNumber[3]:
                        validCard = False    
                    elif cardNumber[1] == cardNumber[2]:
                        validCard = False    
                    elif cardNumber[1] == cardNumber[3]:
                        validCard = False    
                    elif cardNumber[2] == cardNumber[3]:
                        validCard = False                  
                    else:
                        validCard = True    #If the entered input is unique it will set this to True

                    if len(str(cardNumber)) == 4 and validCard:     #This will confirm and end the loop if the length of the card number is 4 and the numbers were unique. if they were not unique it will not end the loop

                        validCardNumber = True      #Ends the loop and confirms that the card number is in the correct format

                    else:
                        print("Error, either the length is incorrect or the card numbers entered were not unique. Please try again")  #Either the length was incorrect (more than 4) or the numbers were not unique.This will inform the user and make the loop ask the user again.
                else:
                    print("Only numbers allowed. Please try again")  #Either the entered input consisted of letters or symbols. This will inform the user and make the loop ask the user again.
            except:
                print("Error Occured, make sure to enter a 4 digit card number. Please try again") #Either an unexpected error occured or the user entered less than 4 digit code.

    #Second part will ask for a PIN number#

    validcurrentPIN = False     #This is used in the while loop and can stop the loop when the condition changes just like (break).
    if validcreate == True:     #This is passed from the main funtion to fully confirm to the program that it can execute the create function
        while not validcurrentPIN:      #This loop will keep asking the user to enter a unique 4-PIN number 
            try:

                currentPIN = input("Enter 4 digit PIN number: ")        #Will ask the user for a unique 4-digit PIN number
                if currentPIN.isdigit():        #An if state to make sure that the string entered is only digit numbers
                    
                    #These if statement will only run if the input was a digit number. It will make sure that the number enter is unique by comparing index values.
                    if currentPIN[0] == currentPIN[1]:
                        validPIN = False        #If the entered digit number is not fully unique it will set this to a boolean variable false
                    elif currentPIN[0] == currentPIN[2]: 
                        validPIN = False
                    elif currentPIN[0] == currentPIN[3]:
                        validPIN = False
                    elif currentPIN[1] == currentPIN[2]:
                        validPIN = False    
                    elif currentPIN[1] == currentPIN[3]:
                        validPIN = False 
                    elif currentPIN[2] == currentPIN[3]:
                        validPIN = False                  
                    else:
                        validPIN = True     #If the entered input is unique it will set this to True

                    if len(str(currentPIN)) == 4 and validPIN:      #This will confirm and end the loop if the length of the PIN number is 4 and the numbers were unique. if they were not unique it will not end the loop
                        validcurrentPIN = True      #Ends the loop and confirms that the PIN is in the correct format
                    else:
                        print("Error, either the length is incorrect or the PIN numbers entered were not unique. Please try again")      #Either the length was incorrect (more than 4) or the numbers were not unique.This will inform the user and make the loop ask the user again.
                else:
                    print("Only numbers allowed. Please try again")      #Either the entered input consisted of letters or symbols. This will inform the user and make the loop ask the user again.

            except:
                print("Error Occured, make sure to enter a 4 digit card number. Please try again")      #Either an unexpected error occured or the user entered less than 4 digit code.

    #Third part will ask for a student Kfupm email

    validEmailLoop = False      #This is used in the while loop and can stop the loop when the condition changes just like (break).
    if validcreate == True:     #This is passed from the main funtion to fully confirm to the program that it can execute the create function
        userEmail = input("Enter your KFUPM email : ")        #Will ask the user for a student KFUPM email.
        while not validEmailLoop:       #A while loop to confirm the correct length of the email.
            if len(userEmail) == 23:    #Usual student emails have a length of 23 including ID and domain
                validEmail = False      #This will be initilized for the next while (Checks the index value of all the entered characters)
                validEmailLoop = True   #This will end the current loop if the length of the email is correct
            else:       #An else statement if the user enters an incorrect email length
                userEmail = input("Wrong email format. Please enter the correct email : ")

        while not validEmail:   #A while loop to confirm the correct format of a KFUPM student email, Will only run if the length of the email is correct

                if userEmail[0].upper() == "G" or userEmail[0].upper() == "S" :     #Will check the index of the first character, It must be s or g (S=Student, G=Graduate)
                    if userEmail[1:10].isdigit():   #The next indexes must be the student ID that consists of only digits
                        if userEmail[10:23].upper() == "@KFUPM.EDU.SA":     #Will check the domain
                            validEmail = True   #If all conditions are true it will end the loop
                        else:       #If the conditions were false it will ask the user again
                            userEmail = input("Wrong email format. Please enter the correct email : ")
                    else:   #If the conditions were false it will ask the user again
                        userEmail = input("Wrong email format. Please enter the correct email : ")
                else:   #If the conditions were false it will ask the user again
                    userEmail = input("Wrong email format. Please enter the correct email : ")

    #Fourth part will ask the user to enter his phone number as an extra service

    extraServiceLoop = False        #This is used in the while loop and can stop the loop when the condition changes just like (break).
    if validcreate == True:         #This is passed from the main funtion to fully confirm to the program that it can execute the create function
        while not extraServiceLoop:     #A while loop to ask the user if they want to add their phone number or not
            validateChoice = input("Do you wish to enter your phone number for added security? (Only KSA numbers supported) - y/n > ")      #Ask the user to accept or decline 
            if validateChoice.lower() == "yes" or validateChoice.lower() == "y":        #If user enters yes then it will start another loop to make sure of the format of the KSA number
                phoneLoop = False   #This is used in the while loop and can stop the loop when the condition changes just like (break).
                while not phoneLoop:   #A while loop to confirm the format of the phone number 
                    phoneNum = input("Enter your Saudi phone number (9665XXXXXXXX) or enter 0 to exit > ")      # Will ask for the phone number.And there is a sentinal value to exit
                    if phoneNum == "0": #if user wishes to exit this if statement will stop all loops
                        validPhone = False #User did not enter a phone number (Boolean value for file writing)
                        phoneLoop = True   #Stops confirmation of phone number loop 
                        extraServiceLoop = True #Stops the main while loop
                    else:   #When the user attempts to enter another input other than 0
                        if len(phoneNum) == 12:     #this is to check for the correct conditions for the number.
                            if phoneNum[0:3] == "966":  #Phone numbers in KSA start with 966. this if will check for that
                                if phoneNum[3] == "5":  #Phone numbers in KSA start with 5 after 966. This if will check for that. 
                                    validPhone = True   #User entered a phone number (for file writing)
                                    phoneLoop = True  #If the phone number starts with 9665 then it is the correct format
                                    extraServiceLoop = True #ends main loop
                                else:
                                    phoneNum = input("Incorrect phone number format.Please Enter your phone number (9665XXXXXXXX) > ") #4 number must be 5. if user enters something else it will ask him again
                            else:
                                phoneNum = input("First three Number must start with 966. Enter your phone number (9665XXXXXXXX) > ") #Incorrect phone number. It will ask again
                        else:
                            phoneNum = input("Wrong phone number length. Enter your phone number (9665XXXXXXXX) > ")#Incorrect phone number. It will ask again

            elif validateChoice.lower() == "no" or validateChoice.lower() == "n":   #If the user does not wish to enter his phone number, this else if statement will check for that.
                phoneLoop = True    #Stops format checking loop
                extraServiceLoop = True #stops main loop
                validPhone = False  #User did not enter a phone number (For file writing)
            else:   #Incorrect input, user must enter the correct input 
                print("Wrong input. Try again.")


    cardFile = str(cardNumber)+".txt"   #Will format a new name for a txt file based on the card number entered (Multiple users)
    Balance = 5000  #An inital balance
    carInsurances = 1500    #User has bills to pay, it is saved in a variable to be written in a txt file to show the user later
    healthInsurance = 750   #User has bills to pay, it is saved in a variable to be written in a txt file to show the user later
    if (validEmail and validPIN) and validCard :  #If the email,PIN and card numbers are valid then it will start saving them in a txt file, must be in if statement so it doesn't save incorrect input
        outFile = open(cardFile, "w")   #Starts writing a new txt file
        outFile.write("Card number: "+ cardNumber + "\n")   #Saves card number in the first line
        outFile.write("PIN number: " + currentPIN + "\n")   #Saves PIN number in the second line 
        outFile.write("Email: " + userEmail + "\n")         #Saves emails in the third line 
        outFile.write("Blanace: "+ str(Balance) +"\n")      #Saves balance in fourth line

        if validPhone:  #If the user entered a phone number then it will write the phone number in a txt file
            outFile.write("Phone Number: "+ str(phoneNum) +"\n") #Saves phone number in fifth line
        else:   #If user did not enter a phone number
            outFile.write("Phone Number: None" + "\n")      # If user did chose not to wirte their phonenumber, it will write none

        outFile.write("Car insurance Bill #1: " + str(carInsurances) + "\n")    #bill will saved in the txt file
        outFile.write("Health insurance Bill #2: " + str(healthInsurance) + "\n")   #bill will saved in the txt file
        outFile.close() #Closes the file
        time.sleep(2)   #the program will sleep for a couple of seconds
        validLogin = True #A boolean value
        login(validLogin,counterOfTransactions) #will CALL the login function AND validLogin will be passed to confirm login


#Done by Ali
def login(validLogin,counterOfTransactions):   #This function allows the user to login to their account bases on the information on the saved txt file

    correctCard = False     #This is used in the while loop and can stop the loop when the condition changes just like (break).
    if validLogin:     #This is passed from the create funtion to fully confirm to the program that it can execute the create function
        while not correctCard:  #A while loop which allows the user to login, It will ask for the card number first
                try:    #Try will check for any incorrect inputed values or wrong file names
                    
                    testCardNumber = int(input("To log in please enter your card number: "))        #asks user for input (Card number)
                    cardFile = str(testCardNumber)+".txt"       #Will format a new name for a txt file based on the login card number entered (Multiple users)
                    outFile = open(cardFile, "r")       #Opens a file on read mode
                    all_Lines = outFile.readlines()  # will turn into a list with a number of indexes

                    first_Line = all_Lines[0]    #  this will give us the card number
                    split_First_Line = first_Line.split(":")  #this will spilt the word and the numbers

                    if testCardNumber == int(split_First_Line[1]):  #Will compare input with what is written in the list
                        second_Line = all_Lines[1] #this will give us the PIN number
                        split_Second_Line = second_Line.split(":") #this will split the word and the number
                        PIN_Loop = False    #This is used in the while loop and can stop the loop when the condition changes just like (break).
                        while not PIN_Loop:     #This loop wil check PIN number for login
                            try:
                                
                                testPIN = int(input("Please enter your PIN number: ")) #this will take the number needed to compare with the test PIN number

                                if testPIN == int(split_Second_Line[1]):    #Compares input with what is written the txt file
                                    PIN_Loop = True     #If true then it will end the loop after the following code is executed

                                    #Checking for phone number
                                    originalPhone = all_Lines[4]        #will check the line of the phones number which is saved in the list all_Lines
                                    splitOriginalPhone = originalPhone.split(": ")  #Splits and saves strings into a list
                                    fileNumber = splitOriginalPhone[1]      #Will save the value of the phone number in the txt file to a variable
                                    if fileNumber == "None\n":      #will check if the phone number in the txt file is none or the user did not enter in the create funtions 
                                        correctCard = True      #If there is prevoius phone number then it will end the loop
                                        bank_menu(cardFile,counterOfTransactions)   #Redirects to bank menu

                                    else:       #If the number in the txt file consists of a value other than "None" this code will run 
                                        fileNumberLoop = False      #This is used in the while loop and can stop the loop when the condition changes just like (break).          
                                        while not fileNumberLoop:   #A while loop to check login input matches to what is in the txt file
                                            try:        #Will check if the input has any errors (letters will result in an error)
                                                userPhone = int(input("Please enter your KSA phone number: "))      #Asks user for phone number
                                                if userPhone == int(fileNumber):        #Compares the input with the txt file phone number
                                                    correctCard = True      #If input phone number matches with txt file then it will end main loop 
                                                    fileNumberLoop = True   ##If input phone number matches with txt file then it will end phone number loop
                                                    bank_menu(cardFile,counterOfTransactions)   #will redirect to bank menu if all conditions are true and pass the card file name according the the input of card number

                                                else:
                                                    print("Phone number does not match.") #Informs the user that the input does not match with txt file
                                            except ValueError:
                                                print("Wrong phone number. Please try again.")  #Informs the user he may entered a wrong number
                                    
                                else:
                                    print("Wrong PIN. Please try again ") #informs the user that he has entered the wrong PIN number
                            except ValueError:
                                print("Please enter the correct PIN number")    #informs the user that he has entered the wrong PIN number
                    else:
                        print("Please enter the correct card number")   #informs the user that he has entered the wrong PIN number

                except ValueError:
                    print("Please enter the correct card number")   #informs the user that he has entered the wrong Card number

                except IOError:
                    print("There is no user with that card number.")    #If there is no txt file with the inputed card number then it will raise an error letting the user know that he has entered the wrong card number
                    exitInput = input("Do you wish to exit the program? Please enter (y) to exit or (n) to try again  >  ") #If the user does not even have an account he will have the option to exit or try again
                    if exitInput.lower() == "y" or exitInput.lower() == "yes" :     #if user has entered yes or y then it will execute the body
                        sys.exit()      #Exists program if the user enters yes or y
                    elif exitInput.lower() == "n" or exitInput.lower() == "no": #if user has entered yes or y then it will execute the body
                        print("Try entering your card number again.")   #Will print the message and then restart the loop and asks the user to try again
                    else:
                        print("Input not recognized. Try to log in again.")     #if the user entes an incorrect exit input, it will let the user know.

#Done by Nawaf
def bank_menu(cardFile,counterOfTransactions):      #Will print and pass the arguments of the bank menu
    print("Bank account program")
    #Simple for loop to print the interface of the menu       
    for x in range(1,3):
        for y in range(1,12):
            print("-"*y, end="")
        print()

    print('''

    1.  Show account information
    2.  Change PIN number
    3.  Withdraw amount of money
    4.  deposit amount of money
    5.  Pay bills
    6.  View the last transactions
    7.  Terminate a program 

    ''')

    for x in range(1,3):
        for y in range(1,12):
            print("-"*y, end="")
        print()
    feature = input("Enter your feature: ")     #Will ask the user to enter which action they wish to make next
    print()
    validFeature = False    #This is used in the while loop and can stop the loop when the condition changes just like (break).
    while not validFeature:     #A while loop which will redirect the user to the function according to their input
            #All if and else if but the last one include a special funtion in regards to the action the user wishes to take
            if feature == "1":  #if user enters 1 it will show information of user
                validFeature = True #ends the loop
                show(cardFile,counterOfTransactions)    #Redirects to   desired function    
            elif feature=="2":  #if user enters 2 it will allow the user to change his PIN
                validFeature = True
                changePINFun(cardFile,counterOfTransactions) 
            elif feature=="3":  #if user enters 3 it will allow the user to withdraw money from their bank account
                validFeature = True
                withdrawFun(cardFile,counterOfTransactions) 
            elif feature=="4":  #if user enters 4 it will allow the user to deposit money to their bank account
                validFeature = True
                depositFun(cardFile,counterOfTransactions) 
            elif feature=="5":  #if user enters 5 it will allow the user to pay their bills (will deduct from their balance)
                validFeature = True
                payBillFun(cardFile,counterOfTransactions) 
            elif feature=="6":  #if user enters 6 it will show all transactions made
                validFeature = True
                viewTransactionsFun(cardFile,counterOfTransactions) 
            elif feature=="7":  #if user enters 7 it will show the recent transactions made during the session (NOT ALL TRANSACTIONS)
                validFeature = True
                terminateFun(cardFile,counterOfTransactions)
            else:   #If user enteres a wrong input they will be notified and asked to enter it again
                print("Wrong input. Please enter your feature.")
                feature = input("Enter your feature: ")

#Done by Nawaf
def show(cardFile,counterOfTransactions):   #This function will show the information of the user
    showFile = open(cardFile,"r")   #opens txt file depending on the name of the card number
    showLines = showFile.readlines()    #Reads files and stores the info in a list
    showFeature = showLines[0:5]    #Make a new list showing only the first 5 lines
    for line in showFeature:    #Prints each element in the list line by line
        print(line)
    time.sleep(3)   #Program sleeps for 3 seconds
    bank_menu(cardFile,counterOfTransactions)   #Redirects to bank menu

#done by Ali
def changePINFun(cardFile,counterOfTransactions): 
    validPIN  = False
    while not validPIN : #This is used in the while loop and can stop the loop when the condition changes just like (break).
        try:
            
             newPIN = input("Enter new 4 digit PIN number or enter the original PIN to exit: ")#takes the pin from the user
             if newPIN.isdigit():#checks if the input is only digits


                if   newPIN[0] == newPIN[1]:        #these lines of statemets are to check for repetitions
                    validnewPIN = False
                elif newPIN[0] == newPIN[2]: 
                    validnewPIN = False
                elif newPIN[0] == newPIN[3]:
                    validnewPIN = False
                elif newPIN[1] == newPIN[2]:
                    validnewPIN = False    
                elif newPIN[1] == newPIN[3]:
                    validnewPIN = False 
                elif newPIN[2] == newPIN[3]:
                    validnewPIN = False  
                else:
                    validnewPIN = True      #the loop breaks after all conditions are satisfied

                if len(str(newPIN)) == 4 and validnewPIN:   #checks for length
                    validPIN  = True
                    outFile = open(cardFile,"r")
                    replacment = ("PIN number: "+newPIN+"\n")
                    #this is to replace the PIN index later on 
                    fileList = outFile.readlines()
                    #this changes it to a list with indexes and to save the data (becuase it will be deleted when we start writing)
                    fileList[1] = replacment
                    #this is where we replace the old PIN with the new one using indexes
                    outFile = open(cardFile,"w")
                    outFile.writelines(fileList)
                    #both of the lines above are to rewrite the card,email,and new PIN.
                    outFile.close()
                    time.sleep(2)
                    bank_menu(cardFile,counterOfTransactions)
                else:
                    print("Wrong PIN number please try again")
        except ValueError:
                print("Wrong PIN number please try again")




#done by both students
def withdrawFun(cardFile, counterOfTransactions): 

    outFile = open(cardFile,"r") #opens in reading mode   
    originalList = outFile.readlines() #puts the contents of the file in a list        
    newBalanceList = []#makes a new empty list

    for element in originalList:
        newBalanceList.append(element.strip())#strips the original list and puts it in the newbalance list

    onlyBalanceList = newBalanceList[3].split(": ")#to seperate between the numbers and letters
    money = float(onlyBalanceList[1])#saves money as the Balance in the file



    validWithdraw = False
    while not validWithdraw: #This is used in the while loop and can stop the loop when the condition changes just like (break).
        try:
            withdrawnMoney = float(input("Enter the amount of money you want to withdraw, or enter 0 to exit: "))#takes the amount of money from the user
            validWithdraw = True
        except ValueError:
            print("Please enter a number.")


    withdrawCheck = False
    validMoney = False
    while not validMoney:   #This is used in the while loop and can stop the loop when the condition changes just like (break).  
        if withdrawnMoney <= money and withdrawnMoney >= 0 :#checks if the user has enough money in the balance and if the entered value is a negative or a positive
            withdrawCheck = True
            validMoney = True
        else:
            while not withdrawCheck:
                try:
                    withdrawnMoney = float(input("Error. Enter the correct amount of money to withdraw (Enter a positive digit) or enter 0 to exit: "))#takes a new value from the user
                    if withdrawnMoney <= money and withdrawnMoney >= 0 :#checks if the user has enough money in the balance and if the entered value is a negative or a positive
                        withdrawCheck = True
                        validMoney = True
                            
                    else:
                        withdrawnMoney = float(input("Error. Enter the correct amount of money to withdraw (Enter a positive digit) or enter 0 to exit: "))
                        if withdrawnMoney <= money and withdrawnMoney >= 0 :

                            withdrawCheck = True
                            validMoney = True
                        else:
                            withdrawnMoney = float(input("Error. Enter the correct amount of money to withdraw (Enter a positive digit) or enter 0 to exit: "))

                except ValueError:
                    print("Please enter a digit number.")


        if float(withdrawnMoney) <= money and withdrawnMoney > 0:#checks if the value entered meets the conditions 
            outFile = open(cardFile,"w")#open file in writing mode
            money = money - withdrawnMoney #deducts the money inputted by the money in the balance               
            money = str(money)#changes to string to make it easier to implimnet in the file 
            balanceInFile = ("Balance: " + money +"\n")#this is used later to replace the old balance with the new        
            originalList.pop(3)#this is to get rid of the old balance 
            originalList.insert(3,balanceInFile)#replaces the old balance with the new one
            for element in originalList:#writes the list again in the file
                outFile.write(element)
            # datetime object containing current date and time
            now = datetime.now()
            # format in dd/mm/YY H:M:S

            dateAndTime = now.strftime("Date of (Withdrawn " + str(withdrawnMoney) + " Riyals) transaction %d/%m/%Y %H:%M:%S \n")
            outFile.write(dateAndTime)#this line and the dateAndTime line above it is used to impliment the date and time intot the transaction
            counterOfTransactions = counterOfTransactions + 1#adds 1 to the counter just incase the user chooses the terminate function
            
            outFile.close()#closes the file 
            time.sleep(2)#the programe sleeps 
            bank_menu(cardFile,counterOfTransactions)#goes back to menu
        outFile.close()#closes the file 
        time.sleep(2)#the programe sleeps 
        bank_menu(cardFile,counterOfTransactions)#goes back to menu
#done by both students
def depositFun(cardFile,counterOfTransactions):

    outFile = open(cardFile,"r") #opens file in reading   
    originalList = outFile.readlines() #saves the file as a list        
    newBalanceList = []#creates a new empty list


    validDeposit = False
    while not validDeposit: #This is used in the while loop and can stop the loop when the condition changes just like (break). 
        try:
            depositMoney = float(input("Enter the amount of money you want to deposit, or enter 0 to exit: "))#takes input from user
            validDeposit = True
        except ValueError:
            print("Please enter a number.")



    for element in originalList:
        newBalanceList.append(element.strip())
        #this module is to get the balance from the file and change it 

    onlyBalanceList = newBalanceList[3].split(": ")#used to split the numbers from the letters
    money = float(onlyBalanceList[1])#this is to identify the balance in the file

   
    depositCheck = False
    validMoney = False
    while not validMoney:  #This is used in the while loop and can stop the loop when the condition changes just like (break).    
        if depositMoney < 0 :#checks for negatives
            print("You cannot add negative balance.")
        
            while not depositCheck:
                try:
                    depositMoney = float(input("Error. Enter the correct amount of money you want to deposit, or enter 0 to exit: "))#asks for input 
                    if depositMoney >= 0:#condition that checks for negaitves
                        depositCheck = True
                        validMoney = True
                        
                    else:
                        depositMoney = float(input("Error. Enter the correct amount of money you want to deposit, or enter 0 to exit: "))#asks for input
                        if depositMoney >= 0 :#checks for negatives
                            depositCheck = True
                            validMoney = True

                except ValueError:#used if the user enters a letter
                    print("Please enter a digit number.")
        
        if depositMoney > 0:    #so we check for negative values
            outFile = open(cardFile,"w")#opens in writing mode
            money = money + depositMoney#adds the amount added by the user to the balance

            money = str(money)#to  make it easier to impliment into the list later 
            balanceInFile = ("Balance: " + money +"\n")#this is the one to replace the old value
            originalList.pop(3)#to remove the old value from the list
            originalList.insert(3,balanceInFile)#to input the new value into the list
            for element in originalList:#this is to write it the information in the list in the file again
                outFile.write(element)
            now = datetime.now()        #This will give the real time of the world
            # format in dd/mm/YY H:M:S  #below it will save it just like the format
            dateAndTime = now.strftime("Date of (Deposited " + str(depositMoney) + " Riyals) transaction %d/%m/%Y %H:%M:%S \n") #to show the deposit transaction time
            counterOfTransactions = counterOfTransactions + 1   #The speical counter for terminate function
            outFile.write(dateAndTime)
            outFile.close()     #Closes file
            time.sleep(2)       #program sleeps for 2 seconds
            bank_menu(cardFile,counterOfTransactions)   #Redirects to bank menu
        outFile.close()     #Closes file
        time.sleep(2)       #program sleeps for 2 seconds
        bank_menu(cardFile,counterOfTransactions)   #Redirects to bank menu


#Done by both students
def payBillFun(cardFile,counterOfTransactions):

    outFile = open(cardFile, "r") #Opens and reads file
    allLines = outFile.readlines()  #after opening the file it puts it in a list and saves it
    billsLines = allLines[5:7]  #this is to sepecify the lines with the bills in them
    onlyBillsList = []  #empty list to save the bills later
    for element in billsLines: #Takes the bill lines and splits : then appends to newer list
        x = element.split(": ")     #Splits :  so it can be seperated by numerical values 
        onlyBillsList.append(x[1])  #Appends to new list, index 1 is the value in list [string,value] 
        
        
    #Reads how much money the user has
    BalanceList = [] #Empty list to save balance line in txt file
    for element in allLines:    #for loop that reads all values in index
        BalanceList.append(element.strip()) #strip removes \n and append adds it to new list. 

    onlyBalanceList = BalanceList[3].split(": ")    #We know that the balance is in the 4th line so we put index 3, onlyBalaceList is [balance:,float number]
    money = float(onlyBalanceList[1])   #saves the numerical value of the list to a variable


    #Prints all bills for the user to see
    showFile = open(cardFile,"r") #opens file and read it
    showLines = showFile.readlines()    #Reads all lines and stores them in a list
    showBills = showLines[5:7]  #we store the indexes of the bills according to their lines
    print("Please choose which bill do you want to pay.")   #notifies the user 
    print()
    for line in showBills:  #Prints bills lines
        print(line)

    #Check which bill the user wants to pay
    billLoop = False        #This is used in the while loop and can stop the loop when the condition changes just like (break).
    while not billLoop:     #This loop will ask the user to enter the number of the bill.  
        try:        #Try will make sure no errors pass by

            billNumber = input("Choose which bill to pay or enter 0 to exit:  ")       #Asks users to enter the number of the bill
                                                
            if billNumber == "1":   #if user enters 1
                if onlyBillsList[0] == "Paid\n":    #If user has already paid this bill it will notify the user
                    print("You have already paid this bill")
                    billLoop = True
                    time.sleep(2)
                    bank_menu(cardFile,counterOfTransactions)  #will redirect to bank menu
                else:   #If user has not paid the bill
                    lowBalance= False   #This is used in the while loop and can stop the loop when the condition changes just like (break).
                    while not lowBalance:   #A while loop which will check several conditions before paying the bill

                        if float(money) > float(onlyBillsList[0]):  #If user has more money than the amount of the bill then the bill be deducted and its status will be "Paid"
                            money = float(money) - float(onlyBillsList[0])  #deducts moeny from balance 
                            newMoney = "Balance: " + str(money) +"\n"   #New variable to repalce old balance line
                            onlyBillsList[0] = "Paid\n" #since the bill has been paid, it's status will change to paid
                            
                            paidStatus = ("Car insurance bill #1: " + onlyBillsList[0])#this is the new value of the bill   
                            allLines.pop(5)#removes the old value
                            allLines.insert(5,paidStatus)#inserts the new value

                            allLines.pop(3)#removes the old money value
                            allLines.insert(3, newMoney)#inserts the new money value
                            outFile = open(cardFile, "w")#opens file in writing mode
                            for element in allLines:#this is to write the data in the file again
                                outFile.write(element)
                            now = datetime.now()    #This will give the real time of the world
                            # format in dd/mm/YY H:M:S
                            dateAndTime = now.strftime("Date of (Paid bill with value " + str(1500) + " Riyals) transaction %d/%m/%Y %H:%M:%S \n")#to write the transaction time 
                            counterOfTransactions = counterOfTransactions + 1#to add to the counter just incase the user choose terminate
                            outFile.write(dateAndTime)  #Writes date and time of transaction
                            outFile.close() #Closes file
                            billLoop = True
                            lowBalance = True
                            time.sleep(2)   #program sleeps for 2 seconds
                            bank_menu(cardFile,counterOfTransactions)
                                
                        
                        else:
                            print("You do not have enough Balance. You will be redirected to the bank menu.")
                            time.sleep(2)
                            bank_menu(cardFile,counterOfTransactions)
                            
                                
            elif billNumber == "2":#if user inputs bill 2
                if onlyBillsList[1] == "Paid\n":#checks if it has been paid or not
                    print("You have already paid this bill")
                    billLoop = True
                    time.sleep(2)
                    bank_menu(cardFile,counterOfTransactions)
                else:
                    lowBalance= False
                    while not lowBalance: #This is used in the while loop and can stop the loop when the condition changes just like (break). 

                        if float(money) > float(onlyBillsList[1]):#checks if the user has enough money to pay for the bill
                            money = float(money) - float(onlyBillsList[1])#deducts the value of the bill from the user's balance
                            newMoney = "Balance: " + str(money) +"\n"#to update the user's balance 
                            onlyBillsList[1] = "Paid\n"#changes the value of the bill to be "paid"
                            
                            paidStatus = ("Health insurance bill #2: " + onlyBillsList[1])  #makes it so if the users chooses to see the bills again the SHOWN value will also be "Paid"
                            allLines.pop(6)     #removes old value
                            allLines.insert(6,paidStatus)       #inserts new value
                            

                            allLines.pop(3) 
                            #removes the old money value
                            allLines.insert(3, newMoney)
                            #inserts the new money value
                            outFile = open(cardFile, "w")
                            #opens file in writing mode
                            for element in allLines:
                                #writes the data in the file again
                                outFile.write(element)

                            billLoop = True
                            lowBalance= True
                            now = datetime.now()        ##This will give the real time of the world
                            # format in dd/mm/YY H:M:S
                            dateAndTime = now.strftime("Date of (Paid bill with value " + str(750) + " Riyals) transaction %d/%m/%Y %H:%M:%S \n")
                            counterOfTransactions = counterOfTransactions + 1
                            #adds to the counter just incase the user chooses the termination option
                            outFile.write(dateAndTime)
                            outFile.close()
                            #closes the file
                            time.sleep(2)
                            #program sleeps for 2 seconds
                            bank_menu(cardFile,counterOfTransactions)
                        
                        
                        else:
                            print("You do not have enough Balance. You will be redirected to the bank menu.")
                            time.sleep(2)
                            bank_menu(cardFile,counterOfTransactions)

            elif billNumber =="0" :
                billLoop = True
                time.sleep(2)
                bank_menu(cardFile,counterOfTransactions)
            else:
                print("Please choose a bill number or enter 0 to exit.")
        except ValueError:
            print("Something went wrong, try again.")


#done by both students
def viewTransactionsFun(cardFile,counterOfTransactions):    #This function will prints all transactions made within the lifetime history of the account
    outFile = open(cardFile,"r")    #Opens file and reads it
    allLinesList = outFile.readlines()  #Reads all lines and stores them to a list
    if len(allLinesList) > 7:   #The first 7 lines are reserved to account info and bills, any lines after them are the transactions
        lastTransaction = allLinesList [7:] #It will store the transactions to a list
        for element in lastTransaction: #Will store every element in the transactions list
            print(element)  #Prints the transactions
        outFile.close() #Closes file
        time.sleep(2)   #program sleeps for 2 seconds
        bank_menu(cardFile,counterOfTransactions) #Redirects to bank menu

    else: # if there are no lines after the user info lines then that means there were no transactions made
        print("No transactions.") #Informs the user that there were no transactions made
        outFile.close() #Closes file
        time.sleep(2)   #program sleeps for 2 seconds
        bank_menu(cardFile,counterOfTransactions)   #Redirects to bank menu




#Done by both students
def terminateFun(cardFile,counterOfTransactions): #This function will print the most recent transactions during the session and then ends the program

    outFile = open(cardFile,"r")        #Opens the file to read
    allLinesList = outFile.readlines()  #Read the entire file and then stores it in a list
    newAllLines = allLinesList[::-1]    #This will simply reverse the list in order to read the last transactions based on the number of transactions made during the session

    if counterOfTransactions > 0:   #This special counter is to see if there are recent transaction made during the run time of the program
        for x in newAllLines[0:counterOfTransactions]:  #It will take the reversed list then it will print the first transaction made till the last transaction only made during the run time of the program
            print(x)  #print the transactions
    else:
        print("No Recent transactions.") #if the special counter is zero then it means the user did not make any transactions such as withdrawing or paying bill,

    outFile.close()     #Closes the file
    sys.exit()  #exits the program 



main()      #This will start running the program and executes the funtion main() which will ask the user to either sign up or login
