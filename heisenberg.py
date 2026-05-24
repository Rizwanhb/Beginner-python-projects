"""
In quantum mechanics, the act of observing a particle changes its momentum. In this game,
 every time you guess where the "electron" is, your observation causes it to jump to a new location!
"""

import random

def play_game():
    print("⚛️ Welcome to the Quantum Uncertainty Game ⚛️")
    print("I'va hidden electron from position 1 to 10 and momentum (1-10)")
    print("Rule: The closer you get to one, the more wildely the other one shifts!")

    #defining position and momentum
    pos=random.randint(1,10)
    mo=random.randint(1,10)
    attempts=0

    #asking from user until they get it right
    while True:
        try:
            guess_pos = int(input("Guess the positon(1-10): "))
            guess_mo=int(input("Guess the momentum (1-10): "))

            #cautions if guess it outside 1-10 for both inputs
            if not (1<= guess_pos <=10 and 1<= guess_mo <=10):
                print("Please keep both guesses between 1 to 10")
                continue

            #adding attempts
            attempts +=1

            #getting both correct

            if guess_pos==pos and guess_mo==mo:
                print(f"\n🏆 IMPOSSIBLE! You perfectly measured position and momentum simultaneously in {attempts}, You broke physics!!")
                break

            #calculatehow far off the guesses are
            dist_pos = abs(guess_pos - pos)
            dist_mo = abs(guess_mo - mo)

            print(f"position was off by {dist_pos}")
            print(f"Momentum was off by {dist_mo}")

            #The uncertanity principle mechanics
            if guess_pos==pos:
                print(f"you guessed the correct position of particle! Momentum becomes highly uncertain!")
                mo = random.randint(1,10)
                pos = max(1,min(10, pos + random.choice([-1,1])))

            elif guess_mo==mo:
                print(f"You gueesed the correct momentum but position becomes highly  uncertain!")
                pos = random.randint(1,10)
                mo = max(1, min(10, mo + random.choice([-1,1])))

            else:
                #The closer you get to one the further away other goes
                #max shift is 4, min shift is 0
                shift_pos=random.choice([-1,1]) * max(0, (4- dist_mo))
                shift_mo = random.choice([-1,1]) *max(0,(4- dist_pos))

                pos=max(1, min(10, pos+shift_mo))
                mo = max(1,min(10, mo + shift_pos))


            print(f"The system has evolved...\n")

        except ValueError:
            print(f"Please enter valid integers. \n")




play_game()







