account_name = input("Enter your account name: ")
current_balance = 1000
print(f"Welcome {account_name}! Your starting balance is ${current_balance}")

def deposit(amount):
    global current_balance
    current_balance += amount
    print(f"Deposited ${amount}. New balance: ${current_balance}")

def withdraw(amount):
    global current_balance
    if amount > current_balance:
        print("Insufficient funds!")
    else:
        current_balance -= amount
        print(f"Withdrew ${amount}. New balance: ${current_balance}")

def check_balance():
    print(f"Current balance: ${current_balance}")

while True:
    print("\nWhat do you want to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
        with open("transactions.txt", "a") as file:
            file.write(f"Deposited ${amount}\n")
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
        with open("transactions.txt", "a") as file:
            file.write(f"Withdrew ${amount}\n")
    elif choice == "3":
        check_balance()
        with open("transactions.txt", "a") as file:
            file.write(f"Checked balance: ${current_balance}\n")
    
    if choice == "4":
        print("Goodbye!")
        with open("transactions.txt", "a") as file:
            file.write("Exited the program\n")
        break

with open("transactions.txt", "r") as file:
    print("Transaction History:")
    content = file.read()
    print(content)