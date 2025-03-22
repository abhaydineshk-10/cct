attended=int(input("Enter the number of classes attended: "))
total=int(input("Enter the total number of classes: "))
percentage= attended/total*100
if percentage<75:
    print("Not allowed to sit in the exam due to low attendance of", percentage, "%")
else:
    print("Allowed to sit in the exam")