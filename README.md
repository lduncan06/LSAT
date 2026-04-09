# LSAT
CS32 Project

import random
# List of sample questions with easy answers -- to be edited
qa_list = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of the sky on a clear day?", "answer": "Blue"},
    {"question": "Who wrote Romeo and Juliet?", "answer": "Shakespeare"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who painted the Mona Lisa?", "answer": "da Vinci"},
    {"question": "What year did World War II end?", "answer": "1945"},
]

# Randomly output a question from the pre-provided list
selected = random.choice(qa_list)

# Ask for input
user_answer = input(f"Question: {selected['question']}\nYour answer: ").strip()

# Compare input to answer of question (case-insensitive comparison)
if user_answer.lower() == selected['answer'].lower():
    # Output 'Correct'
    print("Correct!")
else:
    # Output the actual answer
    print(f"Sorry, the correct answer is: {selected['answer']}")
