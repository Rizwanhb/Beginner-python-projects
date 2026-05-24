"""In this programe we take input of int from user and double it, but the exceeding limit is 
100 so while printing we should look that it doesn't exceed 100 limit"""


#Take input from user
number = int(input("Enter a number: "))

#Create a loop that will print results until it hits 100 limit
while number<=100:
    #Double the number by multiplying it by 2.
    number = number*2
    print(number)
