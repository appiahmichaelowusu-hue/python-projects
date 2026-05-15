import datetime
past_entries = []
while True:
    print("\n1. Write new entry")
    print("2. View all entries")
    print("3. Search entries")
    print("4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        chapter=input("Enter the chapter title: ").title()
        content=input("Enter the content for the chapter: ")
        current_date=datetime.datetime.now()
        past_entries.append(chapter)
        with open("journal.txt", "a") as file:              
            file.write(f"Chapter: {chapter}\n")
            file.write(f"Content: {content}\n")
            file.write(f"Date: {current_date}\n\n") 
    elif choice == "2":
        with open("journal.txt", "r") as file:
            print(f"\nJournal Entries:")
            content=file.read()
            print(content)
    elif choice == "3":
         search_term=input("Enter a search term to find in past entries: ")
         with open("journal.txt", "r") as file:
             content=file.read()
             if search_term.lower() in content.lower():
                 print(f"Found entry: {content}")
             else:
                 print("No matching entry found.")  
    else:
            print("Exiting the journal. Goodbye!")
            break

with open("journal.txt", "r") as file:
    print(f"\nJournal Entries:")
    content=file.read()
    print(content)