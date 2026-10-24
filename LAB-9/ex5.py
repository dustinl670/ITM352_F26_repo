# Conver this dictionary of quiz questions into a JSON file.
import json

questions = {
    "What is the capital of France?: ": ["Paris", "Berlin", "Rome", "Madrid"],
    "What is the capital of Germany?: ": ["Paris", "Berlin", "Rome"],
    "The Mona Lisa was painted by who?: ": ["Leonardo DaVinci", "Vincent van Gogh", "Pablo Picasso"],
}

filename = "quizquestions.json"

with open(filename, "w") as file:
    json.dump(questions, file, indent=4)

print(f"Quiz questions have been saved to {filename}")