# Interactive quiz system, second version.
# Make a list with the questions and correct answers.
# Name: Dustin Lopera
# Date: October 2, 2026

questions = [
    {"question": "What is the capital of France?: ", "answer": "Paris"},
    {"question": "What is the capital of Germany?: ", "answer": "Berlin"},
    {"question": "The Mona Lisa was painted by who?: ", "answer": "Leonardo DaVinci"}
]

for q in questions:
    question = q["question"]
    correct_answer = q["answer"]
    answer = input(f"{question}") 
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}', not '{answer}'")