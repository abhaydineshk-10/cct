balance = 5000
print("Your current balance is: ", balance)
withdraw= int(input("Enter the amount you want to withdraw: "))
if withdraw > balance:
    print("Insufficient balance")
elif withdraw<0:
        print("Invalid amount")
else:
    balance = balance - withdraw
    print("Your remaining balance is: ", balance)