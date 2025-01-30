# Hangman Game 🎯
## Overview
This is a simple Hangman game implemented in Python. The game randomly selects a hidden word from a text file and challenges the player to guess it letter by letter before running out of attempts.

## Features
✅ Random word selection from a .txt file
✅ ASCII-based hangman visuals
✅ User-friendly command-line interface
✅ Input validation for repeated and invalid guesses
✅ Adjustable number of attempts

## How It Works
The game reads words from a text file (words.txt).
A random word is chosen as the hidden word.
The player guesses letters one at a time.
If the letter is correct, it is revealed in the word.
If incorrect, an attempt is lost, and the hangman drawing progresses.
The game ends when the player either guesses the word correctly or runs out of attempts.
## Installation & Usage
Clone this repository:
bash
Copy
Edit
git clone https://github.com/your-username/hangman-game.git
cd hangman-game
Ensure you have Python 3+ installed.
## Run the game:
bash
Copy
Edit
python hangman.py
Make sure words.txt exists in the same directory, containing a list of words (one per line).
Example words.txt
Copy
Edit
python
developer
computer
programming
algorithm
Contributing
Feel free to contribute by adding new features, improving the code, or expanding the word list.
