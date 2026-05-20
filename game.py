import random
user_choice=input("Enter choice (rock,paper or scissors):").lower()
list=["rock", "paper", "scissors"]
computer_choice=random.choice(list)
print(f"Computer chose:{computer_choice}")

if computer_choice== "rock "and user_choice=="paper":
    print("YOU WIN!!!!")
elif computer_choice=="paper" and user_choice=="scissors":
    print("YOU WIN!!!!")
elif computer_choice=="scissors" and user_choice=="rock":
    print("YOU WIN!!!!")
elif computer_choice==user_choice:
    print("DRAWW TRY AGAIN")
else:
    print("YOU ARE A FAT LOOSER!!!!")

