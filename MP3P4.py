'''
Number Guessing Game
'''

import random


def guessing_game():
    global num
    while True:
        print ("MENU:")
        print ("[1] - Play Number Guessing Game")
        print ("[2] - Exit")
        
        choice = input ("Enter your choice from (1-2): ")
        if choice == "1":
            num = (random.randint(0,100))
            # print(num)
            attemps = 0
            while True:
                guess = int(input("Guess the number (1-100): "))
                if guess == num:
                    attemps += 1
                    print(f"Congratulations! You guessed the numbner in {attemps} attempt(s).")
                    break
                elif guess > num:
                    attemps += 1
                    print("Too high!")
                elif guess < num:
                    attemps += 1
                    print("Too low!")
        elif choice == "2":
            print ("Thank you for playing!")
            break 
        else:
            print ("Invalid Choice!")
    
guessing_game()
