password= input("Enter your password: ")
if len(password)<6:
    print("Weak password")
elif password.isalpha() or password.isdigit():
    print("Weak password")
else:
    print("Strong password")