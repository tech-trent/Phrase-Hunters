
# Import your Game class

# Reasons for this are explained on line 26
from .game import Game
from time import sleep                                                                  

# Create your Dunder Main statement
if __name__ == "__main__":

    # Inside Dunder Main:
    ## Create an instance of your Game class
    game = Game()
    
    # Start your game by calling the instance method that starts the game loop
    game.start()

    while True:
        # If the user's input isn't something along the lines of "no", start a new game, otherwise quit
        if not input("\nWould you like to play again? [Y/N] ").lower() in ("n", "no"):  
            print()
            game = Game()
            game.start()
        else:
            print("\nThanks for playing! Goodbye!")
            # The program will display the goodbye message for 3 seconds before shutting down
            sleep(3)                                                                    
            quit()