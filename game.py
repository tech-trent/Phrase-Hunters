
# Create your Game class logic in here

# `Phrase` is imported into and used by `game.py`
from .phrase import Phrase         
# Used to take random phrases     
from random import choice as choose     

class Game:
    # `init` method that initializes all the requested attributes, which are all used later
    def __init__(self):     
        self.missed = 0
        self.phrases = (
            "Take me out to the ball game",
            "We gonna rock down to electric avenue",
            "Medium rare steak please",
            "Please keep your hands and feet inside the vehicle at all times",
            "We live on the most boring street in the country"
        )
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        print("Welcome to Phrase Hunters! Good luck!\n")

    # Sets the phrase that will be used in this particular game
    def get_random_phrase(self):        
        return choose(self.phrases)

    def get_guess(self):
        while True:
            # Guesses must be stored as uppercase, otherwise `phrase.display` will not work properly
            guess = input("\nGuess a letter: ").upper()        
            # Logic for checking if the guess is a single letter
            if guess.isalpha() and len(guess) == 1:         
                return guess
                break
            else:
                # This will print indefinitely until the input function recieves an ideal input
                print("\nPlease type a single letter!")     

    # A boolean is passed to this method that denotes whether the player has won or lost
    def game_over(self, won: bool):     
        if won:
            print("\nCongratulations! You guessed the phrase!")
        else:
            print("\nYou ran out of lives! Better luck next time!")
    
    def start(self):
        # Choose a phrase to use throughout the game
        self.active_phrase = self.get_random_phrase()   
        # Pass that phrase to a new instance of the `Phrase` class
        phrase = Phrase(self.active_phrase)             
        print("Welcome to Phrase Hunter! When prompted, guess a letter. 5 incorrect guesses and the game will end!\n")
        while True:
            # Always display the phrase first, updated with the user's guesses
            phrase.display(self.guesses)    
            # If `phrase.hidden_phrase` has been updated and now matches the phrase chosen by the game, the player has won. Pass `True` to `game_over` and break the main loop
            if phrase.check_complete():     
                self.game_over(True)
                break
            # If the user has guessed incorrectly more than 4 times, they have lost. Pass `False` to `game_over` and break the main loop
            elif self.missed > 4:           
                self.game_over(False)
                break
            # If the player hasn't won or lost yet, we know their gameplay is still in progress
            guess = self.get_guess()        
            # If the letter is present in the phrase (either uppercase or lowercase), add it to the list of guesses, thus ensuring the next call of `phrase.display` when the loop repeats will be up-to-date
            if phrase.check_letter(guess):  
                self.guesses += guess
            # Otherwise, the player has guessed incorrectly. Add a value of 1 to their `missed` guesses and print a warning message
            else:                           
                self.missed += 1
                print(f"\nYou have {5 - self.missed} out of 5 lives remaining!")
            # Make some whitespace, simply for formatting purposes
            print()                         