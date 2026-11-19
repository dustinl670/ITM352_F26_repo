# Application to manage the quiz webapp
# Name: Dustin Lopera
# Date: Nov. 13, 2026

from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import json
import random
from pathlib import Path
from datetime import datetime, timezone
 
# Initial global values/how the quiz progress is tracked.
score = 0
question_number = 0

# Read the question pool from a JSON file.
def load_question_data(file_path):
    with file_path.open(encoding="utf-8") as file:
        return json.load(file)

question_file = Path(__file__).with_name("ASSN1QUESTIONS.json") # Locates question file
question_data = load_question_data(question_file)

high_score_file = Path(__file__).with_name("high_score.json") # Locates high-score file

def load_high_score(): # Reads the saved high score.
    try:
        return int(high_score_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return 0
    
# Converts question data to a list (first listed answer is correct)
all_questions = [
    {
        "question": text,
        "options": details["answers"],
        "correct_answer": details["answers"][0],
        "hint": details["hint"],
    }
    for text, details in question_data.items()
]

# Picks a max of 5 questions and shuffles choices every time the app loads
max_questions = min(5, len(all_questions))
selected_questions = random.sample(all_questions, max_questions)
questions = [
    {
        **question,
        "options": random.sample(question["options"], len(question["options"])),
    }
    for question in selected_questions
]

app = Flask(__name__)
# Flask uses this key to sign the user's session cookie.
app.secret_key = 'team_rocket_keycard'

# Reset quiz progress and shows the intro page
@app.route('/')
def index():
    session.clear()
    session['score'] = 0
    session['question_number'] = 0
    session['wrong_answers'] = []

    # Save a question selection and option order in the session.
    indexes = random.sample(range(len(all_questions)), max_questions)
    session['question_indexes'] = indexes
    session['option_orders'] = [
        random.sample(range(len(all_questions[i]['options'])), len(all_questions[i]['options']))
        for i in indexes
    ]
    
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST']) # Display questions/handles answer submits and navigation.

def quiz():
    score = session.get('score', 0)
    question_number = session.get('question_number', 0)

    # Records the start time (only first request of the quiz)
    if 'quiz_start' not in session:
        session['quiz_start'] = datetime.now(timezone.utc).timestamp()
    if request.method == 'POST':
        # Move on only after the user presses Next.
        if request.form.get('action') == 'next':
            question_number += 1
            session['question_number'] = question_number
            session.pop('answer_feedback', None)
        # Compares the selected answer and stores incorrect answers for review.
        elif question_number < max_questions: 
            correct_answer = questions[question_number]["correct_answer"]
            if request.form.get('answer') == correct_answer:
                score += 1
                session['score'] = score
                session['answer_feedback'] = "Nice work, rookie!"
            else:
                session['answer_feedback'] = (f"Sorry trainer! The correct answer was: {correct_answer}"
                )
                wrong_answers = session.get('wrong_answers', [])
                wrong_answers.append({
                    'question': questions[question_number]['question'],
                    'your_answer': request.form.get('answer'),
                    'correct_answer': correct_answer
                })
                session['wrong_answers'] = wrong_answers
            session['score'] = score
            return redirect(url_for('quiz'))
        
    # To render next question
    if question_number < max_questions:
        return render_template('quiz.html',
                            question=questions[question_number]['question'], 
                            question_number=question_number,
                            options=questions[question_number]['options'],
                            hint=questions[question_number]['hint'],
                            answer_feedback=session.get('answer_feedback'),
                            wrong_answers=session.get('wrong_answers', [])
    )

    # Saving final score and time taken.
    if 'completed_score' not in session:
        session['completed_score'] = score

    if 'time_taken' not in session:
        end = datetime.now(timezone.utc).timestamp()
        session['time_taken'] = round(end - session['quiz_start'], 1)
    
    # Updates the saved high score if this current attempt beats it.
    high_score = load_high_score()
    if score > high_score:
        high_score = score
        high_score_file.write_text(str(high_score), encoding="utf-8")


    session.pop('answer_feedback', None)
    return render_template(
        'result.html',
        score=score,
        max_questions=max_questions,
        high_score=high_score,
        time_taken=session.get('time_taken'),
        wrong_answers=session.get('wrong_answers', [])
    )

# Shows the completed score and time stored in the user's session.
@app.route('/result')
def result():
    global max_questions
    score = session.get('completed_score', 0)
    return render_template(
        'result.html',
        score=score,
        max_questions=max_questions,
        high_score=load_high_score(),
        time_taken=session.get('time_taken')
    )

# This file stores API score submissions separately from the leaderboard.
score_file = Path(__file__).with_name("scores.json1")

# Accepts a name and score as JSON and attach entry to score file.
@app.route('/api/scores', methods=['POST'])
def save_score():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    username = data.get("username")
    submitted_score = data.get("score")

    if not isinstance(username, str) or not username.strip():
        return jsonify({"error": "Username is required"}), 400

    if type(submitted_score) is not int or not 0 <= submitted_score <= max_questions:
        return jsonify({"error": "Invalid score"}), 400

    entry = {"username": username.strip(), "score": submitted_score}
    with score_file.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")

    return jsonify(entry), 201

# Returns a random set of questions without revealing correct answers.
# AI USAGE NOTE: I wasn't sure how restful APIs retrieve questions or how the code is typically laid out, so Copilot helped me implement this endpoint.
@app.route('/api/questions', methods=['GET'])
def get_questions():
    selected = random.sample(all_questions, max_questions)

    return jsonify([
        {
            "question": question["question"],
            "options": random.sample(question["options"], len(question["options"])),
            "hint": question["hint"],
        } for question in selected
    ])

# Store the leaderboard as a JSON object keyed by case-insensitive names.
leaderboard_file = Path(__file__).with_name("leaderboard.json")

# Saves each name's best score and displays the top ten and the player's rank.
# ***AI USAGE NOTE: I used Copilot to help implement the leaderboard function, which included sorting the leaderboard/handling top scores (a part I couldn't figure out).
@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    try:
        entries = json.loads(leaderboard_file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        entries = {}

    if request.method == 'POST':
        completed_score = session.get('completed_score')
        name = request.form.get('name', '').strip()

        if completed_score is None:
            return "Complete the quiz first.", 400
        if not name or len(name) > 40:
            return "Enter a name between 1 and 40 characters.", 400

        key = name.casefold()
        if key not in entries or completed_score > entries[key]['score']:
            entries[key] = {'name': name, 'score': completed_score}

        leaderboard_file.write_text(
            json.dumps(entries, ensure_ascii=False),
            encoding="utf-8"
        )
        session['leaderboard_name'] = key
        return redirect(url_for('leaderboard'))

    # Sorting higher scores first.
    ranked = sorted(
        entries.items(),
        key=lambda item: (-item[1]['score'], item[0])
    )
    top_scores = [
        (entry['name'], entry['score']) for _, entry in ranked[:10]
    ]
    player_rank = next(
        (rank for rank, (key, _) in enumerate(ranked, 1)
         if key == session.get('leaderboard_name')),
        None
    )

    return render_template(
        'leaderboard.html',
        top_scores=top_scores,
        player_rank=player_rank
    )

# Runs the Flask development server when this file is executed directly.
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
    