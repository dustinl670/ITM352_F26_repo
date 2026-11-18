# Application to manage the quiz webapp
# Name: Dustin Lopera
# Date: Nov. 13, 2026

import flask
from flask import render_template, request, redirect, session, url_for
import json
from pathlib import Path
import random
 
# Global variables
score = 0
question_number = 0
question_file = Path(__file__).with_name("ASSN1QUESTIONS.json")
with question_file.open(encoding="utf-8") as file:
    question_data = json.load(file)

high_score_file = Path(__file__).with_name("high_score.json")

def load_high_score():
    try:
        return int(high_score_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return 0
    

all_questions = [
    {
        "question": text,
        "options": details["answers"],
        "correct_answer": details["answers"][0],
        "hint": details["hint"],
    }
    for text, details in question_data.items()
]
max_questions = min(5, len(all_questions))
questions = random.sample(all_questions, max_questions)

app = flask.Flask(__name__)

@app.route('/')
def index():
    global score, question_number, questions
    score = 0
    question_number = 0
    questions = random.sample(all_questions, max_questions)
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, question_number, max_questions, questions

    if request.method == 'POST':
        if question_number >= max_questions:
            return redirect(url_for('quiz'))
        
        answer = request.form.get('answer')
        correct_answer = questions[question_number]["correct_answer"]

        is_correct = answer == correct_answer # Compares selected answer with the correct answer
        if is_correct:
            score += 1
        question_number += 1

    if question_number < max_questions:
        # Render the next question
        return render_template('quiz.html', 
                               question=questions[question_number]['question'], 
                               question_number=question_number,
                               options=questions[question_number]['options'],
                               hint=questions[question_number]['hint'])
    else:
        # Save the score when it sets a new record.
        high_score = load_high_score()
        if score > high_score:
            high_score = score
            high_score_file.write_text(str(high_score), encoding="utf-8")

        return render_template(
            'result.html',
            score=score,
            max_questions=max_questions,
            high_score=high_score
        )
answer_feedback = session.get('answer_feedback', None)

@app.route('/result')   
def result():
    # Display the final score
    global score, max_questions
    return render_template(
        'result.html',
        score=score,
        max_questions=max_questions,
        high_score=load_high_score()
    )

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
    