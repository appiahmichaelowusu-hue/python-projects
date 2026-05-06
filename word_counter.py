user_text=input("Enter a statement: ")
def count_words(text):
    words=text.split()
    return len(words)

print("Number of words in the statement is:", count_words(user_text))
parts=user_text.split()
counts=[]
for part in parts:
    count=0
    for i in range(len(parts)):
        if part==parts[i]:
            count+=1
    counts.append(count)
most_counts=max(counts)
if most_counts==1:
    print("There are no repeated words.")   
else:
    print(f"The most repeated word is '{parts[counts.index(most_counts)]}' and it appears {most_counts} times.")           
unique_words=set(parts)
number_of_unique_words=len(unique_words)
print(f"There are {number_of_unique_words} unique words in the statement.")