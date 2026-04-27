students=[]
scores=[]
for i in range(5):
    name=input("Enter the name of student: ")
    score=int(input("Enter the score of student: "))
    students.append(name)
    scores.append(score)
average_score=sum(scores)/len(scores)

with open("class_assessment.txt", "a") as file:
    for i in range(len(students)):
        file.write(f"{students[i]}: {scores[i]}\n")
    file.write(f"Average score of class: {average_score}\n")
with open("class_assessment.txt", "r") as file:
    content=file.read()
    print("Updated class_assessment.txt with average score:")
    print(content)
