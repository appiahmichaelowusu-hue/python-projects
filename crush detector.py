text_first=input('Do they text you first? (yes/no) '),
remember=input('Do they remember small details about you? (yes/no) ')
make_time=input('Do they make time for you? (yes/no) ')
compliment=input('Do they compliment you? (yes/no) ')
jealous=input('Do they get jealous when you talk about people? (yes/no) ') 

scores=[]
if text_first=='yes':
    scores.append(1)
if remember.lower()=='yes':
    scores.append(1)
if make_time.lower()=='yes':
    scores.append(1)
if compliment.lower()=='yes':
    scores.append(1)
if jealous.lower()=='yes':
    scores.append(1)

total_sum=sum(scores)
with open("crush_report.txt", "w") as file:
    file.write(f"Total Score: {total_sum}\n")
    if total_sum==5:
        file.write("They are definitely into you. Stop thinking and shoot your shot! \n")
    elif total_sum>=3: 
        file.write("There are signs. But don't read too much into it yet. \n")
    elif total_sum>=1:
        file.write("Probably just being friendly. Manage your expectations. \n ")
    else:
        file.write("They don't even know you exist. Time to move on. \n")

with open("crush_report.txt", "r") as file:
    report=file.read()
    print(report)
               