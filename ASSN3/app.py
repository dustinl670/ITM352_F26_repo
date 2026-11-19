# Application to manage the quiz webapp
# Name: Dustin Lopera
# Date: Nov. 13, 2026

import flask
from flask import render_template, request, redirect, session, url_for, jsonify
import json
import random
from pathlib import Path
 
# Global variables
score = 0
question_number = 0

question_file = Path(__file__).with_name("ASSN1QUESTIONS.json") # Finding data path for the questions.
with question_file.open(encoding="utf-8") as file:
    question_data = json.load(file)

high_score_file = Path(__file__).with_name("high_score.json") # Locates high-score file.

def load_high_score(): # Reads the saved high score.
    try:
        return int(high_score_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return 0
    
# Converting JSON file to a question dictionary.
all_questions = [
    {
        "question": text,
        "options": details["answers"],
        "correct_answer": details["answers"][0],
        "hint": details["hint"],
    }
    for text, details in question_data.items()
]

max_questions = min(5, len(all_questions)) # Determines max # of questions.
selected_questions = random.sample(all_questions, max_questions) # Randomly picks questions from JSON file pool
questions = [
    {
        **question,
        "options": random.sample(question["options"], len(question["options"])),
    } # Shuffles options each time.
    for question in selected_questions
]

app = flask.Flask(__name__)
app.secret_key = 'team_rocket_keycard'

@app.route('/')
def index():
    global score, question_number, selected_questions
    score = 0
    question_number = 0
    questions = random.sample(all_questions, max_questions)
    session.pop('answer_feedback', None)
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, question_number, max_questions, questions

    if request.method == 'POST':
        if request.form.get('action') == 'next':
            question_number += 1
            session.pop('answer_feedback', None)
        elif question_number < max_questions:
            correct_answer = questions[question_number]["correct_answer"]
            if request.form.get('answer') == correct_answer:
                score += 1
                session['answer_feedback'] = "Nice work, rookie!"
            else:
                session['answer_feedback'] = (f"Sorry trainer! The correct answer was: {correct_answer}"
                )
            return redirect(url_for('quiz'))
        
    # Render the next question
    if question_number < max_questions:
        return render_template('quiz.html',
                            question=questions[question_number]['question'], 
                            question_number=question_number,
                            options=questions[question_number]['options'],
                            hint=questions[question_number]['hint'],
                            answer_feedback=session.get('answer_feedback')
    )
    
    high_score = load_high_score()
    if score > high_score:
        high_score = score
        high_score_file.write_text(str(high_score), encoding="utf-8")


    session.pop('answer_feedback', None)
    return render_template(
        'result.html',
        score=score,
        max_questions=max_questions,
        high_score=high_score
    )

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
    