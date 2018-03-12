# Hangman Game
This is a simple Hangman game done in Python. 

## How to run
1. To run this game you need to make sure you have **Python** installed on your machine. Except for that - it's really easy.
2. **Download** this directory as a **ZIP file** by pressing the big green button *Clone or Download* -> *Download ZIP*.
3. **Unzip** the folder.
4. As soon as you have the *hangman-master* folder unzipped, you need to launch *hangman.py*. You can do this using various methods (like CMD *for Windows*, Terminal *for MacOS*, Standard Python IDLE to open the file + F5 to run it *works on every platform*).
5. Enjoy!

## How to play
The game is fairly simple: algorithm randomly chooses a noun from the file called *words.txt* and your goal is to **guess** what this word is letter by letter.
When you launch the file, you'd see something like this in your console:

```
Welcome to the HANGMAN game!
Note: if you run this program on MacOS, input letters in 'speech marks' while guessing.

Word: ********
Healths: 10
Guess a letter: 
``` 

Guess some letter and input it, then press *ENTER*. If your letter is present in the word - algorithm will change some of the stars to show you the position(s) of the letter in the word:

```
Guess a letter: m

Word: *mm*****
Healths: 10
Guess a letter: 
```

If you guessed wrong - one health point will be taken away from you:

```
Guess a letter: a
Word: *mm*****
Healths: 9
Guess a letter:
```

Continue until you figure it out or run out of health points. At the end you will receive a message according to your result. They look like this:

```
Congratulations! You won! The word was IMMUNITY.

```
```
Well... It was a nice try anyways. The word was IMMUNITY.
```

## Progress

If you ever want to check your progress - open the *log.txt* file. There you can find all the information about your previous runs (won or lost, how long did it take, what was the word):

```
WON in 34 seconds for the word IMMUNITY
LOST in 41 seconds for the word INTELLIGENT
```