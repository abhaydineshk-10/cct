bill= float(input("Enter the total bill amount: "))
tip= int(input("Enter the tip percentage: "))
if bill<0 or tip<0:
    print("Invalid tip percentage")
elif tip>100:
    print("Invalid tip percentage")
else:
    tip_amount= bill*tip/100
    print("The tip amount is: ", tip_amount)
    print("The total amount is: ", bill+tip_amount)