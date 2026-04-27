candidate_1="Michael"
print(f"First candidate: {candidate_1}")
candidate_2="Sarah"
print(f"Second candidate: {candidate_2}")
candidate_3="David"
print(f"Third candidate: {candidate_3}")
user_input = input("Enter the name of the candidate you want to vote for (or 'exit' to finish): ")
vote_1=0
vote_2=0
vote_3=0

while True:
    if user_input.lower() == 'exit':
        print("Voting finished.")
        break
    elif user_input == candidate_1:
        print(f"You voted for {candidate_1}.")
        vote_1 += 1
        print(f"Current votes for {candidate_1}: {vote_1}")     
    elif user_input == candidate_2:
        print(f"You voted for {candidate_2}.")
        vote_2 += 1
        print(f"Current votes for {candidate_2}: {vote_2}")
    elif user_input == candidate_3:
        print(f"You voted for {candidate_3}.")
        vote_3 += 1
        print(f"Current votes for {candidate_3}: {vote_3}")
    else:
        print("Invalid candidate. Please try again.")
    user_input = input("Enter the name of the candidate you want to vote for (or 'exit' to finish): ")

with open("voting_results.txt", "w") as file:
    file.write(f"{candidate_1}: {vote_1} votes\n")
    file.write(f"{candidate_2}: {vote_2} votes\n")
    file.write(f"{candidate_3}: {vote_3} votes\n")
    if vote_1 > vote_2 and vote_1 > vote_3:
        file.write(f"The winner is {candidate_1} with {vote_1} votes.\n")
    elif vote_2> vote_1 and vote_2 > vote_3:
        file.write(f"The winner is {candidate_2} with {vote_2} votes.\n")
    else:
        file.write(f"The winner is {candidate_3} with {vote_3} votes.\n")


with open("voting_results.txt", "r") as file:
    print("Voting Results:")
    content=file.read()
    print(content)
