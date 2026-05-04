import time
import difflib

print("Welcome to the Typing Speed Test!")
input("Press Enter to start the test...")
test_text = "I love programming in Python. It is a versatile and powerful language that allows me to create amazing projects and solve complex problems. The more I learn, the more I realize how much there is to explore in the world of coding."
print("\nType the following text as fast as you can:")
print(test_text)
start_time = time.time()
user_input = input("\nYour input: ")
end_time = time.time()
time_taken = end_time - start_time
accuracy = difflib.SequenceMatcher(None, test_text, user_input).ratio() * 100
words=len(user_input.split())
wpm= (words/time_taken)*60
print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Words per minute: {wpm:.2f}")

with open("typing_speed_results.txt", "a") as file:
    file.write(f"Time taken: {time_taken:.2f} seconds, Accuracy: {accuracy:.2f}%, WPM: {wpm:.2f}\n")
with open("typing_speed_results.txt", "r") as file:
    print("\nTyping Speed Results:")
    content= file.read()
    print(content)

wpm_value = []
with open("typing_speed_results.txt", "r") as file:
    for line in file:
        parts= line.split(",")
        if len(parts) >= 3:
            try:
                wpm_part = parts[2].strip()
                if wpm_part.startswith("WPM: "):
                    wpm_value.append(float(wpm_part.replace("WPM: ", "")))
            except ValueError:
                pass
    wpm_value.sort(reverse=True)  # sorts highest to lowest
print("Top 3 Scores:")
for i in range(min(3, len(wpm_value))):
    print(f"{i+1}. {wpm_value[i]} WPM")