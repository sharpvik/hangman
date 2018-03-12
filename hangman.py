#
# Hangman game
#

# imports
from random import randint
import time

# read the file 
f = open("words.txt", "r")
words = f.readlines()
f.close()

# format the document
for i in range(0, len(words)):
    words[i] = words[i].replace("\n", "")

# select a word
def word_select():
    r = randint(0, len(words))
    chosen_word = words[r]
    return chosen_word

# letter guessing ang validation 
def letter_guess():
    l = str(input("Guess a letter: "))
    if l == "" or len(l) > 1:
        l = letter_guess()
    return l



# define class Hangman
class Hangman:
    def __init__(self, word):
        self.word = word
        self.stars_letters = "*" * len(word)
        self.letters_used = []
        self.healths = 10

    def word_return(self):
        return self.word.upper()

    def stars_letters_return(self):
        return self.stars_letters

    def letter_apply(self, letter):
        indexes = []
        if letter not in self.letters_used and letter in self.word:
            for i in range(0, len(self.word)):
                if self.word[i] == letter:
                    indexes.append(i)
            for index in indexes:
                arr = list(self.stars_letters)
                arr[index] = letter
                self.stars_letters = "".join(arr)
        elif letter in self.letters_used:
            print("ERROR: This letter has been used before!")
        else:
            self.healths_decrement()
        self.letters_used.append(letter)

    def healths_return(self):
        return self.healths

    def healths_decrement(self):
        self.healths -= 1

    def is_alive(self):
        if self.healths > 0:
            return True
        else:
            return False

    def is_solved(self):
        if "*" not in self.stars_letters:
            return True
        else:
            return False



# initialize the game
def game_init():
    w = word_select()
    game = Hangman(w)
    result = ""
    start = int(round(time.time())) # starts the stopwatch
    print("\nWelcome to the HANGMAN game!\nNote: if you run this program on MacOS, input letters in 'speech marks' while guessing.")
    while game.is_alive() and (not game.is_solved()):
        print("\nWord: {}".format(game.stars_letters_return()))
        print("Healths: {}".format(game.healths_return()))
        l = letter_guess()
        game.letter_apply(l)
    if game.is_solved():
        print("\nCongratulations! You won! The word was {}.\n".format(game.word_return()))
        result = "WON"
    else:
        print("\nWell... It was a nice try anyways. The word was {}.\n".format(game.word_return()))
        result = "LOST"
    finish = int(round(time.time())) # stops the stopwatch
    total_time = finish - start # seconds
    # log file
    log = open("log.txt", "a+")
    log.write("{} in {} seconds for the word {}\n".format(result, total_time, game.word_return()))
    log.close()
    # exit
    e = input("Press ENTER to play one more time or input Q to exit: ")
    if e.lower() != "q":
        game_init()

game_init()
