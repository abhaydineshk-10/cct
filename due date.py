due_days= int(input("Enter the number of days due: "))
if due_days<0:
    print("Invalid due date")
elif due_days<5:
    fine=0
elif due_days<10:
    fine=5
elif due_days<30:
    fine=10
else:
    fine=15
print("Your fine is: ", fine)