import random
option=['rock','paper','scissor']
user=input('Enter your choice:"rock","paper","scissor": ').lower()
if user not in option:
    print("Invalid choice")
else:
    computer=random.choice(option)
    print("Computer's choice: ", computer)
    if user==computer:
        print("It's a tie")
    elif user=="rock" and computer=="scissor":
        print("You won")
    elif user=="paper" and computer=="rock":
        print("You won")
    elif user=="scissor" and computer=="paper":
        print("You won")
    else:
        print("Computer won")
