import random

print("H A N G M A N")
answers = ["python", "java", "swift", "javascript"]
correct_answer = random.choice(answers)
user_answer = input("Guess the word: > ")
if user_answer == correct_answer:
    print("You survived!")
else:
    print("You lost!")
