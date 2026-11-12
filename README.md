# Quiz-App

A simple two-player trivia quiz game built with Python. The game features six animal-related questions, where two players take turns answering questions to earn points. Each player has two attempts per question and can skip a question at any time. At the end of the game, the program compares both players' scores and announces the winner.

## Features

- **Two-Player Mode:** Supports two players competing against each other.
- **Animal Trivia Questions:** Includes six questions about interesting animal facts.
- **Alternating Turns:** Automatically switches between players after each question.
- **Limited Attempts:** Gives each player two attempts to answer each question correctly.
- **Question Skipping:** Allows players to skip questions by typing `skip`.
- **Score Tracking:** Stores and updates each player's score using a dictionary.
- **Answer Verification:** Checks submitted answers against the correct answers, ignoring uppercase and lowercase differences.
- **Winner Determination:** Compares final scores and announces the winner or a draw.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the question dictionary in a file named `question.py`.
3. Save the main game program in a file named `main.py` in the same directory.
4. Open a terminal or command prompt.
5. Run the program:

   ```bash
   python main.py
   ```

6. Enter two player names separated by a space.
7. Take turns answering the questions.
8. Type `skip` if you want to skip a question.
9. View the final scores and winner announcement.

## Example

**Example Input:**

```text
Enter 2 player with a space: John Alice

It is John's turn
What animal can sleep for up to three years at a time?
Enter answer: Snail

Correct answer! One point added...

It is Alice's turn
Which animal has a heart the size of a small car?
Enter answer: Blue whale

Correct answer! One point added...
```

**Example Final Output:**

```text
Congrats to John! The score is 4
```

*Note: This is an illustrative example. Actual scores depend on the players' answers.*

## Concepts Practiced

- **Dictionaries:** Organizing quiz questions, answers, and player scores using nested dictionaries.
- **Functions:** Creating reusable functions for answer verification, player switching, and winner determination.
- **Loops:** Using `for` and `while` loops to manage questions and answer attempts.
- **Conditional Statements:** Checking answers, handling skipped questions, and determining the winner.
- **String Methods:** Using `.lower()` to compare answers without case sensitivity and `.split()` to separate player names.
- **Boolean Values:** Returning `True` or `False` from the answer-checking function.
- **Dictionary Operations:** Using `dict.fromkeys()` to initialize player scores and updating scores dynamically.
- **Indexing:** Switching between players using list indices.

## Language

Python 3
