stored_username='username'
stored_password='password'
username= input("Enter your username: ")
password= input("Enter your password: ")
if username==stored_username and password==stored_password:
    print("Login successful")
else:
    print("Invalid credentials")
