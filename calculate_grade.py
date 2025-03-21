def calculate_grade(marks):
    average= sum(marks)/len(marks)
    if average>=80:
        return "A"
    elif average>=60:
        return "B"
    elif average>=40:
        return "C"
    else:
        return "D"
    marks=[]
    for i in range(3):
        mark= int(input("Enter the marks: "))
        if 0<=marks <=100:
            marks.append(mark)
        else:
            print("Invalid marks")
            exit()
    print("Your grade is: ", calculate_grade(marks))  