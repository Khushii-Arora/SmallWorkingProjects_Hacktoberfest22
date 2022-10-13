import random
from words import words
import string

def legal(words):
    ran=random.choice(words)
    while '-' in words or ' ' in words:
        ran=random.choice(words)
    
    return ran.upper()


def hangman():
    word=legal(words)
    word_letters=set(word)  #getting the letters of the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set()      #what the user has guessed
    lives=[i for i in range(len(word))]
    while len(word_letters)>0 and len(lives)>0:
        print("Letters that you have already used = ",used_letters)

       
        
        user_letter=input("Guess a letter = ").upper()
        
        if user_letter in alphabet- used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives.remove(lives[0]) 
                print("That letter is not in the word.") 
                print()      
        
        elif user_letter in used_letters:
            print("You have already used the letter.Try Again!")
        
        else:
            print("Invalid character, Please try again!")

        word_list=[letter if letter in used_letters else "_" for letter in word ]
        print()
        print("Current word status = ",word_list)
        print("No of lives left = ",len(lives))
        
    
    if len(word_letters)==0:
        print("Yayy!..Congrats you gussed the word!")
        print()
    elif len(lives)==0:
        print("Oops! sorry you lost!, the word was ",word)
        print()
    
hangman()



  