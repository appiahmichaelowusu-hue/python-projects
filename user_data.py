user_name = input("What is your name? ")
user_age = input("What is your age? ")

with open("user_data.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Age: {user_age} years\n")

with open("user_data.txt", "r") as file:
    content = file.read()

print("Data saved to user_data.txt:")
print(content)