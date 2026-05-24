"""
Douglas Hofstadter’s Pulitzer-prize-winning book Gödel, Escher, Bach contains many interesting mathematical puzzles,
 many of which can be expressed in the form of computer programs. 
 In Chapter XII, Hofstadter mentions a wonderful problem:

1.Pick some positive integer and call it n.

If n is even, divide it by two.

If n is odd, multiply it by three and add one.

Continue this process until n is equal to one.
"""

def main():
    #Ask user to input a number
    n = int(input("Enter a number: "))

    #Create while loop to repeat the process until n reaches 1
    while n>1:
        #Make if condition for odd numbers
        if n%2==1:
            print(f"{n} is odd, so I make it 3n+1: {3*n + 1}")
            n=3*n + 1

        else:
            print(f"{n} is even, so I make it half: {n//2}")
            n=n//2


main()