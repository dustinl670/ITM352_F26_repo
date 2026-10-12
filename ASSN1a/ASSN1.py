# Assignment 1: Pokemon Knowledge Quiz.
# Name: Dustin Lopera
# Date: October 11, 2026

from string import ascii_lowercase
import random
import json

print("Hello, Pokemon Trainer! Before we get you out in the field, let's test out your Pokemon Knowledge.")
print("You may ask for assistance anytime by typing \"Jigglypuff, use Helping Hand\" during a question.")
ready = input("Are you ready? Yes/No: ").strip().lower()

if ready != "yes":
    print("Come back when you are ready!")
    exit()

question_file = open("ASSN1QUESTIONS.json", "r")
questions = json.load(question_file)

NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(questions, num_questions):
    num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(alternatives, hint):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    while True:
        answer_label = input("Choice? (Type \"Jigglypuff, use Helping Hand\" for a hint): ").strip().lower()

        if answer_label == "jigglypuff, use helping hand":
            print(f"Hint: {hint}")
        elif answer_label in labeled_answers:
            return labeled_answers[answer_label]
        else:
            print(f"Invalid choice. Choose one of {', '.join(labeled_answers)}.")

def ask_question(question, answers, hint):
    correct_answer = answers[0]
    ordered_answers = random.sample(answers, k=len(answers))
    answer = get_answer(ordered_answers, hint)

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The correct answer is {correct_answer!r}.")
        return 0

# Main program logic starts here.
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0

# Main Loop
for num, (question, details) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(
        question,
        details["answers"],
        details["hint"]
    )

print(f"\nYou got {num_correct} correct.")

try:
    with open("high_score.txt", "r") as score_file:
        high_score = int(score_file.read())
except (FileNotFoundError, ValueError):
    high_score = None

if high_score is None or num_correct > high_score:
    print("Pokemon Master! You set a new high score!")
    with open("high_score.txt", "w") as score_file:
        score_file.write(str(num_correct))
else:
    print(f"Your high score is still {high_score}. Atleast it's not worse than before!")