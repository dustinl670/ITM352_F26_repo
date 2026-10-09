# Interactive Quiz system, second version.
# Have a dictionary with the questions and correct answers.

questions = {
    "What is the capital of France?: ", ["Paris", "Berlin", "Rome", "Madrid"],
    "What is the capital of Germany?: ", ["Paris", "Berlin", "Rome"],
    "The Mona Lisa was painted by who?: ", ["Leonardo DaVinci", "Vincent van Gogh", "Pablo Picasso"],
}

for question, answers in questions.items():
    correct_answer = answers[0]
    answer = input(f"{question}") 
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}', not '{answer}'")