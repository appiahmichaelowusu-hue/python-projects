import sys
import random
user_choice=input("Enter choice (rock, paper or scissors)").lower()
list=["rock","paper","scissors"]
computer_choice=random.choice(list)
print (computer_choice)


if user_choice== "rock" and computer_choice=="scissors":
    print("CONGRATULATIONS, YOU WON")
elif user_choice=="paper" and computer_choice=="rock":
    print("CONGRATULATION , YOU WON")
elif user_choice=="scissors" and computer_choice=="paper":
    print("CONGRATULATIONS, YOU WON")
else:
    print("TAKE A HIKE, YOU FAT LOOSER!!!!!!!")