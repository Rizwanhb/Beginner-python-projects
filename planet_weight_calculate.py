"""
In this programe of ours we are gonna calculate if something has some weight on earth,
what weight it's gonna have on different planets of solar system. It's a simple programe
that uses constants and if  statements.
"""

#First we give write each planets gravity or weight in relevence to earth
#Make them outside main funnction so they can be used 
MARS = 0.378
MERCURY = 0.376
VENUS = 0.889
JUPITER = 2.36
SATURN = 1.08
URANUS = 0.815
NEPTUNE = 1.14

#now we create a main function 
def main():
    print("-"*50)
    print("OUTER SPACE WEIGHT CALCULATOR", )
    print("-"*50)
    #First we prompt the user to input their weight or any weight on eath
    earthling = float(input("Enter a weight on Earth:"))

    #Now we ask them what plannet they wanna see their weight on
    planets = input("Enter a planet:").strip().lower()

    #now we are gonna use if,elif and else conditions for all planets
    #We round each answer upto 2 places 
    if planets=='mars':
        mars= earthling * MARS
        print(f"The equivalent weight on Mars: {mars:.2f}")

    elif planets=='mercury':
        mercury=earthling * MERCURY
        print(f"The equivalent weight on Mercury: {mercury:.2f}")

    elif planets=='venus':
        venus=earthling * VENUS
        print(f"The equivalent weight on Venus: {venus:.2f}")

    elif planets=='jupiter':
        jupiter=earthling * JUPITER
        print(f"The equivalent weight on Jupiter: {jupiter:.2f}")

    elif planets=='saturn':
        saturn=earthling * SATURN
        print(f"The equivalent weight on Saturn: {saturn:.2f}")

    elif planets=='uranus':
        uranus=earthling * URNAUS
        print(f"The equivalent weight on Uranus: {uranus:.2f}")

    elif planets=='neptune':
        neptune=earthling * NEPTUNE
        print(f"The equivalent weight on Neptune: {neptune:.2f}")

    else:
        print("Enter a valid planet!!")
        
main()
