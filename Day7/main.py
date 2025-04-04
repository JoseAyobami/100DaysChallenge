import random

from hangman_words import word_list
from hangman_art import hangman_stages, logo

lives = 6

print(logo)

# Ranomly select a word from the word_list and assign to a variable to a variable called chosen_word. Then print it
chosen_word = random.choice(word_list)
print(chosen_word)




# Create a "placeholder"  with the same number of blanks as the chosen_word. 
placeholder = ""
word_length = len(chosen_word)
for postion in range(word_length):
    placeholder += "_"
print(placeholder)   

# Ask the user to guess a letter and assign it to a variable called guess. Make guess a lowercase.
game_over = False
correct_letter = []


while not game_over:

    print(f"******************{lives} /6 LIVES LEFT******************")
    guess = input("Guess a letter: ").lower()
    

    # Check if the user has already guessed the letter. If they have, print "You have already guessed that letter"
    if guess in correct_letter:
        print(f"You have already guessed {guess}")
    
    
     

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# You guessed {guess}, that's not in the word. You lose a life.
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter    
        else:
            display += "_"  
    print(display)  


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")


        if lives == 0:
            game_over = True
            print("******************YOU LOSE******************") 



    if "_" not in display:
        game_over = True     
        print("******************YOU WIN******************")      


    print(hangman_stages[lives])        


     
    
    









