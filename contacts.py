contact_name=input("Contact name : ")
contact_phone_number=input("Contact phone number : ")
with open("contacts.txt", "a") as file :
    file.write(f"{contact_name} : {contact_phone_number}\n")
with open("contacts.txt", "r") as file:
    content=file.read()
    print("Data saved to contacts.txt:")
    print(content)