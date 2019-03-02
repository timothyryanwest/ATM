#Here we create a function named 'account_balance'
##This function is used to print the opening account balance.
def account_balance(acc_balance):   
    print("Your current balance:\n%.2f" %acc_balance)
    
#Now we create a function named 'deposit_amount'
##This function is used to calcuate the deposit amount and display the ending balance.
def deposit_amount(acc_balance):
    deposit_amount = float(input("How much would you like to deposit today?\n"))
    balance = acc_balance + deposit_amount
    print("Deposit was $%.2f, current balance is $%.2f" % (deposit_amount, balance))   

#Here we create a function named 'withdrawal_amount'
##This function is used to reduce the withdrawal amount from the initial balance
##prior to displaying the remaining balance.
###If our user tries to withdraw an amount greater than their current balance, they are informed as such.
def withdrawal_amount(acc_balance):
    withdraw_amount = float(input("How much would you like to withdraw today?\n"))
    if withdraw_amount > acc_balance:
        print("$%.2f is greater than your account balance of $%.2f" % (withdraw_amount, acc_balance))
    else:
        balance = acc_balance - withdraw_amount
        print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdraw_amount, balance))

#This allows the user see their opening balance, and asks for a customized input character. 
acc_balance = float(500.25)
userchoice = input ("What would you like to do? (D) Deposit (W) Withdraw (B) Check balance (Q) Quit\n")

#Here we create an IF/ELIF statement to check the user's input.
##Based on input, the user will be forwarded to the applicable branch function below, or the session is ended.
if (userchoice == 'D'):
    deposit_amount(acc_balance)
elif (userchoice == 'W'):
    withdrawal_amount(acc_balance)
elif (userchoice == 'B'):
    account_balance(acc_balance)
else:
    print('Thank you for banking with us.')