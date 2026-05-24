import math
"""
This is a basic calculator in whic we take we numbers from a user and the operation
they wannna perform between those two number and give a result. We need to import maths,
other than that it's just basic python rules that'll do the job.
"""

print("="*50)
print("WELCOME TO CALCULATOR")
print("="*50)

#Making an emoty list incase user want all the answers they got
l = []

while True:
    try:
    #get the user input for the two numbers
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
    except ValueError:
        print("Enter a valid number!!")
#get their input about the operations they wanna perform beetween those two numbers
    c = input("Enter the operation you wanna perform or (q) to quit: (+,-,/,*,sqrt,%,log,power,square,sin..)")
    if c=='q':
        print("Quitting programe...")
        exit()

    else:
#for dividing with zero case
        if c=='/' and b==0:
            print("Invalid operation can't divide by zero!!")

#for the rest of other operations
        elif c=='+':
            addition=a+b
            print(addition)

        elif c=='-':
            subtraction = a-b
            print(subtraction)

        elif c=='*':
            multiply = a*b
            print(multiply)

        elif c=='/':
            divide = a/b
            print(f"{divide:.3f}")

        elif c=='%':
            percent = (a*b) / 100
            print(f"{a}% of {b} is {percent}")

        elif c=='sqrt':
            if a<0:
                print("Error! can't calculate sqrt of negative number!")
            else:
                sqrt=math.sqrt(a)
                print(f"sqrt of {a} is {sqrt}")

        elif c=='log':
            log = math.log(a)
            print(f"log of {a} is {log:.3f}")

        elif c=='power':
            power = a**b
            print(f"{a} raised to power of {b} is {power}")
        elif c=='square':
            square = a**2
            print(f"square of {a} is {sqaure}")
        elif c=='sin':
            sin=math.sin(a)
            print(f"sin of {a} is {sin:.3f}")
        elif c=='cos':
            cos = math.cos(a)
            print(f"cos of {a} is {cos:.3f}")
        elif c=='tan':
            tan = math.tan(a)
            print(f"tan of {a} is {tan:.3f}")
    

    
