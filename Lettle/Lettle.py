import string
import random
from wordlist import words

def random_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def Lettle():
    word = random_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    attempt=0
    lives = 13    
    while len(word_letters) > 0 and lives > 0:
        print('Only', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
                attempt+=1
            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')
                attempt+=1

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
    if lives == 0:
        print('You ran out of tries. The word was', word)
    else:
        print('Good job! you guessed the word under',attempt,"tries", word, '!!')

Lettle()
input()
