#Hangman
#By: Gabriel Gebril

import random

word_list = ["wish","plate","zany","monkey","sea","excuse","attack","disturbed","steel",
             "bead","expensive","interfere","whisper","request","zip","crooked"]

used_letters = []

hidden_word = []

word = word_list[random.randint(0,15)]

hidden_word = hidden_word + (['_'] * len(list(word)))

game_won = False

number_of_guesses = 5

while game_won == False:
    print("Number of guesses left: ",number_of_guesses)
    print ("You have already used these letters: ", " ".join(used_letters))
    print(" ".join(hidden_word))
    letter_guess = input("Please guess a letter: ")

    good_guess = False
    
    if letter_guess not in used_letters:

        used_letters.extend(letter_guess)
        
        for i in range(0,len(word)):
            if word[i] == letter_guess:
                hidden_word[i] = letter_guess
                good_guess = True
    else:
        letter_guess = input("Please guess a letter you HAVEN'T used before!: ")
        if letter_guess not in used_letters:
            used_letters.extend(letter_guess)
        good_guess = True

    if good_guess == False:
        number_of_guesses = number_of_guesses - 1

    if number_of_guesses == 0:
        break

    if hidden_word.count('_') == 0:
        game_won = True
        break

if game_won:
    print("Congratulations you win!")
else:
    print("Sorry! You lost... Please try again!")
    
    
