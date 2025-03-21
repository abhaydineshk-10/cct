balance= 5000
choice= input("Do you want to deposit(D) or withdraw(w)? ").upper()
if choice not in ["D", "W"]:
    print("Invalid choice")
else:
    amount= int(input("Enter the amount: "))
    if amount<0:
            print("Invalid amount")
    elif choice=="W" and amount>balance:
            print("Insufficient balance")
    else:
        if choice=="D":
                balance= balance+amount
        else:
                balance= balance-amount
        print("Your remaining balance is: ", balance)