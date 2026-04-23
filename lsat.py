# LSAT
CS32 Project

import random
# List of sample questions with easy answers -- to be edited
lsat_questions = [
    {
        "id": 1,
        "type": "Logical Reasoning",
        "text": "All philosophers are thinkers. Some thinkers are logicians. Therefore, some philosophers are logicians. Which of the following exhibits the same flawed reasoning?",
        "options": {
            "A": "All cats are mammals. Some mammals are dogs. Therefore, some cats are dogs.",
            "B": "All birds can fly. Penguins are birds. Therefore, penguins can fly.",
            "C": "Some students are athletes. All athletes are disciplined. Therefore, some students are disciplined.",
            "D": "All roses are flowers. Some flowers are red. Therefore, some roses are red.",
            "E": "No reptiles are warm-blooded. Snakes are reptiles. Therefore, snakes are not warm-blooded."
        },
        "answer": "A",
        "explanation": "The original argument incorrectly assumes that because some thinkers are logicians, those logicians must include the philosophers. Option A makes the same fallacy."
    },
    {
        "id": 2,
        "type": "Logical Reasoning",
        "text": "If it rains, the ground will be wet. The ground is wet. Therefore, it rained. This reasoning is flawed because:",
        "options": {
            "A": "It fails to account for other causes of wet ground.",
            "B": "It confuses necessary and sufficient conditions.",
            "C": "It relies on an unproven causal link.",
            "D": "It uses circular reasoning.",
            "E": "It is a valid argument."
        },
        "answer": "A",
        "explanation": "The argument commits the fallacy of affirming the consequent. Rain leads to wet ground, but wet ground can have other causes (sprinklers, spill)."
    },
    {
        "id": 3,
        "type": "Reading Comprehension",
        "text": "Passage: Some economists argue that minimum wage laws reduce employment. However, studies in high-cost cities show that moderate increases do not lead to job losses. The author's main point is:",
        "options": {
            "A": "Minimum wage laws always hurt employment.",
            "B": "The effect of minimum wage depends on context.",
            "C": "Economists are always wrong about wages.",
            "D": "High-cost cities are exceptions to economic rules.",
            "E": "Minimum wage should be abolished."
        },
        "answer": "B",
        "explanation": "The author provides a counterexample to absolute claims, implying context matters."
    },
    {
        "id": 4,
        "type": "Logical Reasoning",
        "text": "No dogs are reptiles. All poodles are dogs. Therefore, no poodles are reptiles. Is this argument valid?",
        "options": {
            "A": "Yes, it is logically valid.",
            "B": "No, it commits the fallacy of the undistributed middle.",
            "C": "No, it is circular.",
            "D": "Yes, but only if poodles exist.",
            "E": "No, because reptiles could be poodles."
        },
        "answer": "A",
        "explanation": "Valid categorical syllogism: If all poodles are dogs and no dogs are reptiles, then poodles cannot be reptiles."
    },
    {
        "id": 5,
        "type": "Logical Reasoning",
        "text": "A study found that people who eat breakfast weigh less on average. Hence, eating breakfast causes weight loss. Which of the following, if true, most weakens the argument?",
        "options": {
            "A": "People who eat breakfast tend to exercise more.",
            "B": "Skipping breakfast may lead to overeating later.",
            "C": "Breakfast foods are often high in sugar.",
            "D": "The study only surveyed adults.",
            "E": "Some people eat breakfast and are overweight."
        },
        "answer": "A",
        "explanation": "If breakfast eaters also exercise more, exercise could explain weight difference, not breakfast itself."
    }
]

# Continue from 6 to 50 (abbreviated for length; full generator logic shown below)

def generate_lsant_style_questions(start_id, count):
    questions = []
    templates = [
        ("Logical Reasoning", "If {A}, then {B}. {B} occurred. Therefore {A}. This is flawed because...", "Affirming the consequent fallacy."),
        ("Logical Reasoning", "Some {X} are {Y}. All {Y} are {Z}. Therefore, some {X} are {Z}. Is this valid?", "Valid if 'some' means at least one."),
        ("Reading Comprehension", "Passage: {Text}. The author would likely agree with which statement?", "Look for main idea or implicit assumption."),
        ("Logical Reasoning", "Claim: {Statement}. Which of the following, if true, most strengthens the argument?", "Find evidence that supports causal link or generalization."),
        ("Analytical Reasoning", "Five people sit in a row: A, B, C, D, E. A is not next to C. B is next to D. Who must be at an end?", "Deduce from constraints.")
    ]
    # Simplified generation for demo (actual would randomize)
    for i in range(count):
        qid = start_id + i
        qtype = "Logical Reasoning" if i % 3 != 0 else "Reading Comprehension"
        questions.append({
            "id": qid,
            "type": qtype,
            "text": f"Sample question {qid} – More LSAT content here.",
            "options": {chr(65+j): f"Option {chr(65+j)}" for j in range(5)},
            "answer": "C",
            "explanation": "Explanation for question."
        })
    return questions

# Generate 50-100 questions (here we generate 50)
sample_lsat_set = generate_lsant_style_questions(6, 45)  # to reach 50 total from 1-5 above
full_lsat_set = lsat_questions + sample_lsat_set


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
