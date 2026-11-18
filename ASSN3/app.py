# Application to manage the quiz webapp.
# Name: Dustin Lopera
# Date: November 13, 2026

from flask import Flask, render_template, request, redirect, url_for

# Global variables.
score = 0
current_question = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
    }
]

max_questions = len(questions)

app = Flask(__name__)

@app.route('/')
def index():
    global score, question_number
    score = 0
    question_number = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, question_number, max_questions, questions

    if request.method == 'POST':
        # Capture the answer from the form
        answer = request.form.get('answer')

        # Check if answer is correct.
        if answer == questions[question_number]["options"][-1]:
            score += 1
        question_number += 1

    if question_number < max_questions:
        # render the next question
        return render_template('quiz.html',
                               question=questions[question_number]["question"],
                               options=questions[question_number]["options"]
                               )
    else:
        # Quiz is over, render the result page
        return render_template('result.html', score=score)
    
@app.route('/result')
def result():
    global score, max_questions
    return render_template('result.html', score=score, max_questions=max_questions)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()