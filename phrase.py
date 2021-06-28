
# Create your Phrase class logic here

class Phrase:
    def __init__(self, phrase: str):
        # `phrase` is the phrase given my `game.start`, and is the "answer" the user is trying to guess
        self.phrase = phrase      
        # `hidden_phrase` is the most important variable in the game. It's printed every time the main loop runs, and updates whenever the user guesses correctly          
        self.hidden_phrase = ''          
        # This loop simply fills up `hidden_phrase` with spaces and underscores, wherever appropriate based on the shape of the true phrase   
        for char in self.phrase:            
            if char == " ":
                self.hidden_phrase += (" ")
            else:
                self.hidden_phrase += ("_")

    # This method both updates and prints out the `hidden_phrase` attribute, taking into account the user's guesses
    def display(self, update_chars: list):         
        # `hidden_phrase` must be emptied out so that the updated version isn't simply added on top of the existing version            
        self.hidden_phrase = ''                                 
        for phrase_char in self.phrase:
            # Find out whether or not the character in the question is uppercase
            uppercase = phrase_char.isupper()       
            # If the letter in question is one the user has guessed, make sure it shows up in the updated `hidden_phrase`, in its original case
            if phrase_char.upper() in update_chars:             
                if uppercase:
                    self.hidden_phrase += phrase_char.upper()
                else:
                    self.hidden_phrase += phrase_char
            # If the given character isn't actually in the phrase, simply re-iterate the loop in the initializer; add spaces and underscores wherever needed
            elif phrase_char == " ":                            
                self.hidden_phrase += " "
            else:
                self.hidden_phrase += "_"
        # Print out the updated `hidden_phrase` attribute, with the user's guesses added to it
        print(self.hidden_phrase)                               
    
    # Returns `True` if the given letter is present in the phrase in any way
    def check_letter(self, letter: str):                
        return letter.upper() in self.phrase.upper()
    
    # Returns `True` if the `hidden_phrase` attribute has been updated enough to match the original phrase, in which case the user has won.
    def check_complete(self):                           
        return self.hidden_phrase == self.phrase
        