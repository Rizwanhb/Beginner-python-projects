"""We are gonna write a code that will teach addition to user.
More specifically, Our program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99).
 The user should be asked for an answer to the generated problem.
  Our program should determine if the answer was correct or not, and give the user an appropriate message to let them know.
  """

import random

def main():
    print("Addition Academy")
    #generate random number between 10 and 99 
    #Create two different vairable for that
    a=random.randint(10,99)
    b=random.randint(10,99)

    #Ask user the question about the outcome
    print(f"What is {a} + {b}? ")
    
    #Get their input as an answer 
    answer = int(input("Your answer: "))

    #Now set the conditions according to the answer
    if answer != a + b:
        print("Incorrect.")
        print(f"The expected answer is {a + b}")

    else:
        print("Correct!")


main()
