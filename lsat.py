# LSAT
# CS32 Project

import random
import json
import os

def load_questions(filepath = "questions.json"):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filepath} not found!")
        return []

def ask_question(q):
    print(f"\nQuestion {q['id']} ({q['type']}): {q['text']}")
    for option, text in q['options'].items():
        print(f"{option}: {text}")

def shuffle_options(q):
    items = list(q["options"].items())  # [('A', '...'), ('B', '...'), ...]
    random.shuffle(items)
    new_options = {}
    new_answer_label = None
    labels = ['A', 'B', 'C', 'D', 'E']
    for new_label, (old_label, text) in zip(labels, items):
        new_options[new_label] = text
        if old_label == q["answer"]:
            new_answer_label = new_label
    q["options"] = new_options
    q["answer"] = new_answer_label

def get_user_answer():
    while True:
        ans = input("Your answer: ").strip().upper()
        if ans in ['A', 'B', 'C', 'D', 'E']:
            return ans
        print("Please enter A, B, C, D, or E.")

def prompt_continue():
    while True:
        cont = input("Do you want to try another question? (yes/no): ").strip().lower()
        if cont in ['yes', 'y']:
            return True
        if cont in ['no', 'n']:
            return False
        print("Please enter 'yes' or 'no'.")

def main():
    #Track unused questions
    unused_questions = qa_list.copy()
    missed_questions = []

    #Track correct answers of total attempted questions
    total_attempted = 0
    total_correct = 0
    stats = {
        "Logical Reasoning": {"attempted": 0, "correct": 0},
        "Reading Comprehension": {"attempted": 0, "correct": 0},
        "Analytical Reasoning": {"attempted": 0, "correct": 0}
    }

    #Welcome
    print("Welcome to the LSAT Practice App!")

    while True:
        #See whether there are questions left
        if not unused_questions:
            print(f"\nThanks for practicing! Final score: {total_correct}/{total_attempted}")
            break

        #Randomly select from unused questions and remove from list
        selected = random.choice(unused_questions)
        unused_questions.remove(selected)

        #Ask the question
        shuffle_options(selected)
        ask_question(selected)
        user_answer = get_user_answer()
        total_attempted += 1
        q_type = selected['type']
        stats[q_type]["attempted"] += 1

        # Compare input to answer of question (case-insensitive comparison)
        if user_answer == selected['answer']:
            total_correct += 1
            stats[q_type]["correct"] += 1
            # Output 'Correct'
            print("Correct!")
            print(f"Explanation: {selected['explanation']}")
        else:
            #Add to missed questions list
            missed_questions.append(selected)
            # Output the actual answer
            print(f"Sorry, the correct answer is: {selected['answer']}")
            print(f"Explanation: {selected['explanation']}")

        if not prompt_continue():
            if missed_questions:
                print("\nYou missed these questions. Do you want to review them? (yes/no)")
                choice = input("> ").strip().lower()
                if choice in ['yes', 'y']:
                    for q in missed_questions:
                        print(f"\nQuestion {q['id']}: {q['text']}")
                        for opt, text in q['options'].items():
                            print(f"{opt}: {text}")
                        print(f"Correct answer: {q['answer']}")
                        print(f"Explanation: {q['explanation']}")
                print(f"\nThanks for practicing! Final score: {total_correct}/{total_attempted}")
                exit()
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
