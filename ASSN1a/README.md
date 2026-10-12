# This is a file answering the required questions for Assignment #1.
# Name: Dustin Lopera
# Date: October 11, 2026

●      Data Structure Justification: What data structure design was used to store the quiz questions and why is the best for the application? Explain the design quality goals for this? E.g. readability by human, easy to read from a file, etc. Do not simply list the goals. Explain them relative to storing quiz questions.
    # I used the JSON data structure to store the quiz questions. This is a good format because it keeps the data separate from the Python code. This makes it easier to edit questions and makes the code itself less clunky. Also, it's easier to read because you know what the file is for.

●      Function Design: Why did you design your non-trivial custom function the way you did, and what specific problem does it solve in the application?
    # For my get_answer() function, I designed it to handle the retrieval of inputs from the user. It runs a while loop that solves the issue of invalid inputs, continuing the program if a user doesn't use the pre-set selection of labelled answers. Additionally, the loop allows the user to input a string for a hint tailored to the question, with the question being able to be answered with or without the use of one.

●      Control Flow: A brief explanation of how the application handles invalid user inputs (e.g., preventing inputs outside of "a-d") and why you chose that validation loop structure. Explain the design quality goals for this? E.g. Do not simply list the goals. Explain them relative to storing quiz questions[RK1] .
    # My get_answer() function does this by applying labels to the question answer and alternatives (Questions labelled with A-D). Then, it runs a "for" loop to print the labelled answers, followed by a "while" loop that runs the user's input and offers the option for a hint. Then it utilizes an if/elif function to check if the provided input is a labelled answer. If not, it prints "Invalid choice," and tells the user to select one of the labelled answers before running the question again.

    I chose this design function because using "if" is relatively simple and keeps my code easier to understand. This process also makes the quiz more user-friendly and keeps the answers within bounds of reason.

●      Use of AI: You must also include a statement on how you used AI (Copilot or any other tool) in the creation of this assignment.  Be honest: if we ask you to explain your code and you cannot, that will mean that you relied too heavily on AI.
    # For this assignment, I utilized Copilot as a tool to help repair my code whenever I found myself stuck. When I would ask it to generate/fix my code, I also tell it to break it down piece by piece to gain a better understanding of what it created and the reasoning behind it.