# Hangman Game
This is a simple Hangman game done in Python. 

## How to run
1. To run this game you need to make sure you have **Python** installed on your machine. Except for that - it's really easy.
2. **Download** this directory as a **ZIP file** by pressing the big green button *Clone or Download* -> *Download ZIP*.
3. **Unzip** the folder.
4. As soon as you have the *hangman-master* folder unzipped, you need to **launch** *hangman.py*. You can do this using various methods (like CMD *for Windows*, Terminal *for MacOS*, Standard Python IDLE to open the file + F5 to run it *works on every platform*). 
5. Depending on your *Python installation settings* you can use commands like `python hangman.py` or `hangman.py` to launch the file in your console terminal. Be sure to change the path in your terminal to that of the *hangman-master* folder.

*Windows* CMD terminal should look like this:
```
PS C:\path\to\the\folder\hangman-master>
```
*MacOS* or *Linux* terminal should look like this:
```
john@doe:~ path/to/the/folder/hangman-master$
```
[*Windows* CMD Terminal Tutorial - YouTube](https://www.youtube.com/watch?v=MBBWVgE0ewk)

[*MacOS* Terminal Tutorial - YouTube](https://www.youtube.com/watch?v=F1kAm_2d0yo)

[*Linux* Terminal Tutorial - YouTube](https://www.youtube.com/watch?v=oxuRxtrO2Ag)

> To open *Windows CMD* window in this specific folder, you can open the folder, make sure none of the files is highlighted, **left SHIFT + right MOUSE click** hovering over some free space in the folder -> *Open PowerShell window here* or *Open command window here*.
6. **Enjoy!**

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
LOST in 41 seconds for the word INTELLIGENCE
```

## Exit

After each round the game will provide you with two choices: press *ENTER* to play again or input *Q* (doesn't matter upper- or lowercase) to exit.

## Play yourself and share with friends!

I would be flattered if you'd **share** this game with some of your friends and/or **collaborate** here in GitHub.

## Contact

For any personal or business enquiries:
- Email: *sharp.vik@gmail.com*
- [Twitter](https://twitter.com/sharp_vik)
- [VK](https://vk.com/perigrinus)
- [Instagram](https://www.instagram.com/viktooooor) 