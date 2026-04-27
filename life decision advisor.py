while True:
  try:
    first_question=int(input("What is your age? "))
    break
  except ValueError:
    print("Invalid input. Enter a number")
while True:
  try:
    second_question=int(input("What is your monthly income? $"))
    break
  except ValueError:
    print("Invalid input. Enter a number")
while True:
  try:
    third_question=int(input("What are your monthly expenses? $"))
    break
  except ValueError:
    print("Invalid input. Enter a number ")
while True:
  try:
    forth_question=int(input("How many hours do you spend on productive activities daily? "))
    break
  except ValueError:
    print("Invalid input. Enter a number")
while True:
  try:
    fifth_question=int(input("How many hours do you spend on social media daily? "))
    break
  except ValueError:
    print("Invalid input. Enter a number")


with open("life_report.txt", "a")as file:
    file.write(f"Age: {first_question}\n")
    print(f"Age: {first_question}")
    file.write(f"Monthly Income: ${second_question}\n")
    print(f"Monthly Income: ${second_question}")
    file.write(f"Monthly Expenses: ${third_question}\n")
    print(f"Monthly Expenses: ${third_question}")
    file.write(f"Hours spent on productive activities daily: {forth_question}\n")
    print(f"Hours spent on productive activities daily: {forth_question}")
    file.write(f"Hours spent on social media daily: {fifth_question}\n")
    print(f"Hours spent on social media daily: {fifth_question}")


    percentage_income=0.7*second_question

    if third_question>percentage_income:
     file.write("You are living beyond your means.\n")
     print("You are living beyond your means.")
    else:
     file.write("You are living within your means.\n")
     print("You are living within your means.")
    if fifth_question>forth_question:
     file.write("You are wasting more time than you are investing.\n")
     print("You are wasting more time than you are investing.")
    else:
     file.write("You are investing more time than you are wasting.\n")
     print("You are investing more time than you are wasting.")
    hours_per_year_wasted=fifth_question*365
    file.write(f"You are wasting {hours_per_year_wasted} hours per year on social media.\n")
    print(f"You are wasting {hours_per_year_wasted} hours per year on social media.")

    amount_saved=second_question-third_question
    file.write(f"You are saving ${amount_saved} per month.\n")
    print(f"You are saving ${amount_saved} per month.")
    if amount_saved<=0:
     file.write("You save poorly.\n")
     print("You save poorly.")
    else:
     file.write("You save well.\n")
     print("You save well.")
    life_score=100
    if third_question>percentage_income:
     life_score-=20
    if fifth_question>forth_question:
     life_score-=20
    if amount_saved<=0:
     life_score-=20
    file.write(f"Your life score is: {life_score}/100\n")
    print(f"Your life score is: {life_score}/100\n")
with open("life_report.txt", "r")as file:
    print("Detail of Life Report:")
    content=file.read()
    print(content)


