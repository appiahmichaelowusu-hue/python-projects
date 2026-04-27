import random
import string
number_of_char=int(input("How many characters do you want your password to be? "))
def password_generator(number_of_char):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(number_of_char))
    return password
password = password_generator(number_of_char)
print(f"Your generated password is: {password} ")

with open("password.txt", "w") as file:
    file.write(password)
with open("password.txt", "r") as file:
    print("Your password has been saved to password.txt")
    content=file.read()
    print(f"Your password is: {content}")

