#!/usr/bin/env python3

# Guessing Game Template
# Mr. Enrico
# NBHS Intro to Engineering

from random import randint

# Main loop
while True:

    # Initialize game variables at the start of each new game
    lives = 3
    values = 10
    level = 1
    #for a small easter egg
    hint_count=0
    # Number to expand range by each level
    difficulty = 5

    # Choose a secret value
    secret = randint(1, values)
    
    #option to turn on or off hints after each level
    hints_prompt = input(f'Would you like to activate hints? Hints will tell you if the number you guessed is too high or low. [y/n]').lower()
    if hints_prompt == "n":
      print("Hints are disabled, good luck!")
      hints=False
    if hints_prompt == "y":
      hint_count+=1
      print("Hints are enabled.")
      hints=True
    else:
      print("Ok... I'll just take that as a no.")
      hints=False
        
    # Guess loop
    while lives > 0:
        print(f"Lives remaining: {lives}\n")
        try:
 
            guess = int(input(f"I'm thinking of a number between 1 and {values}, what is it? "))
            if guess not in range(1, values+1):
                raise ValueError
        except ValueError:
            guess = None
            print("Please guess a number in the appropriate range.")

        if guess == secret:

            level += 1
            lives += 1
            values += difficulty
            
            #Found a flaw in your game, if you leveled up, the "secret" number stayed exactly the same, so I added this to change the number everytime you level up.
            secret= randint(1, values)
            
            print(f"You got it! Moving on to level {level}. Here's an extra life to help you along.")
            
            #Dialogue for winning the game/beating level 5
            if level==6:
              if hint_count==0:
                
                #no hints easter egg
                print("Woah there, you beat level 5 using no hints at all? You must either have the luck of the gods or be a cheater. Well, idk, so here, have a cookie.")

              win_prompt=input(f"Wow, you officially won the game and beat level 5, congrats! Would you like to continue to infinite level mode? [yes/quit]")
              if win_prompt=="quit":
                break
        else:
            print("Nope, lose a life!")
            lives -= 1
            
            if hints==True:
                if guess>secret:
                  print("The number you guessed was too high")
                if guess<secret:
                  print("The number you guessed was too low")

    print("GAME OVER\n")
    print(f"The number I was thinking of was {secret}.")
    again = input("Play again? [y/n]:").lower()
    if again == "n":
        break
