# Hangman2.0
---
A game written in python designed to teach grades 6-8 about basic game programming and computer logic. With a Camper verison and an instuctor version.

Line 23-26:
```Python
    print("Number of guesses left: ",number_of_guesses)
    print ("You have already used these letters: ", " ".join(used_letters))       #Go though making the game screen and accepting input
    print(" ".join(hidden_word))
    letter_guess = input("Please guess a letter: ")
```

Line 45: 
```Python
        number_of_guesses = number_of_guesses - 1                                #Need to decrease our number of lives if we guess poorly.
```

Line 28: 
```Python
        break                                                                             #break out of the loop to get to the end screen.
```

Line 52 - 52: 
```Python
        game_won = True
        break                                                                             #break out of the loop to get to the end screen.
```
Line 54-57:
```Python
if game_won:
    print("Congratulations you win!")
else:                                                                                               #Figure out if you won or if you lost.
    print("Sorry! You lost... Please try again!")
```

