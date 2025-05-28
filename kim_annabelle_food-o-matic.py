#Annabelle Kim
#randomly generating meals for the user
#April 4, 25
#no bugs
#Incorporated colors, customized menu, customized prices for both mains and flairs, ensuring user enters a valid number
#https://www.w3schools.com/python/python_try_except.asp

import random
#import random library
def print_colored(text, color):
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    print(color_codes.get(color, "") + text + color_codes["reset"])

mains = ['cheeseburger', 'pizza', 'buffalo wings', 'salmon', 'steak tacos', 'chicken quesadillas', 'girlled cheese', 'steak', 'chicken fingers']
#create list with given elements for main menu items
m_prices = [20,17,24,30,25,22,17,32,15]
#create list with given elements for main menu item prices
flairs = ['with french fries', 'with tater tots','with mac and cheese','with baguette','with cesar salad','with vegetables','with chicken soup','with potato wedges','with chips and guacamole']
#create list with given elements for flairs dishes
f_prices = [1,1,3,2,3,1,2,1,3]
#create list with given elements for flair dish prices
while True:
#create forever loop
    try:
    #run through code unless there is a value error
        while True:
        #create forever loop
            item = int(input("How many menu items do you need? (Less than 10):"))
            #set variable equal to the user's input of the question
            if item < 10:
            #if user responds with a number less than 10
                break
                #end forever loop
            else:
            #if the user responds with any other number
                print_colored ("Please enter a number less than 10.","red")
                #display message in red
        for i in range(item):
        #create for loop
            random_color=random.choice(["red","green","yellow","blue","magenta","cyan"])
            #computer chooses a random color from the list
            main = random.choice(mains)
            #computer chooses a random element from the "mains" list
            index = mains.index(main)
            #identify index of random main course choice
            flair = random.choice(flairs)
            #computer chooses a random element from the "flairs" list
            index2 = flairs.index(flair)
            #identify index of random flair dish choice
            price = m_prices[index] + f_prices[index2]
            #add the prices of each randomly seleceted prices from the mains and flairs lists
            print_colored(f"{main} {flair}, ${price}", f"{random_color}")
            #display message in randomly selected color
        break
        #end forever loop
    except ValueError:
    #if user response is not a number
        print_colored ("You did not enter a number. Please try again:","red")
        #display message in red