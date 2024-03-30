print("Welcome to the ATM simulator \n")

balance = 1000

userPin = 1234

atm_on = False

userInput = int(input("Please enter your PIN number: "))

if userInput == userPin:
    print("Correct PIN \n")
    atm_on = True
else:
    print("Incorrect PIN NUMBER")

while atm_on == True:
    decision = input("Please select from the main menu: \nCheck Balance \nDeposit Money \nWithdraw Cash \nExit \n\n")
    if decision.lower() == "check balance":
        print(f"\n {balance} \n")
        break     
    elif decision.lower() == "deposit money":
        depositAmount = int(input("\n How much would you like to deposit: \n"))
        balance = balance + depositAmount
        print(balance)
        break
    elif decision.lower() == "withdraw cash":
        withdrawAmount = int(input("\nHow much would you like to withdraw?: \n"))
        if withdrawAmount > balance:
            print("You do not have the available funds for this transaction.")
        else:
            balance = balance - withdrawAmount
            print(balance)
        break
    elif decision.lower() == "exit":
        print("Goodbye!")
        break
    else:
        print("\n Invalid selection\n ")
        

