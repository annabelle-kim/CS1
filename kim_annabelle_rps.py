#cat                                                                                                                                        #extra credit
import random                                                                                                                               #importing random library
import os                                                                                                                                   #importing os library
score=0                                                                                                                                     #set score to 0
score1=0                                                                                                                                    #set score1 to 0
score2=0                                                                                                                                    #set score2 to 0
score3=0                                                                                                                                    #set score3 to 0
def colored_text(text, color, input_or_print):                                                                                              #create function of printing or inputting color for text
    color_codes = {                                                                                                                         #link color to value
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }

    if input_or_print == "print":                                                                                                           #if colored text is printed
        print(color_codes.get(color, "") + text + color_codes["reset"])                                                                     #print in color
    else:                                                                                                                                   #if colored text is used for anything else
        return input(color_codes.get(color, "") + text + color_codes["reset"])                                                              #print question in color (for input), user response lies in variable
while True:                                                                                                                                 #create forever loop
    RPS = ["rock","paper","scissors"]                                                                                                       #create list
    RPSG = ["rock","paper","scissors","gun"]                                                                                                #create list
    colored_text("Welcome to Rock, Paper, Scissors","cyan","print")                                                                         #print and color text
    user_choice = colored_text("Choose a gamemode! Classic, Rock Paper Scissors Gun, Multiplayer, or Magic 8 Ball:","blue","input")         #user reponse lies in variable and input is in color
    if user_choice=="classic" or user_choice == "multiplayer":                                                                              #if user chooses classic or mulitplayer
        colored_text("Welcome to Classic Rock, Paper, Scissors!","green", "print")                                                          #print text in color
        if user_choice == "classic":                                                                                                        #if user chooses classic
            p2_name = "bot"                                                                                                                 #the variable p2_name equals bot
        else:
            p2_name = colored_text("Name:", "red", "input")
        while True:
            user = colored_text("Choose Rock, Paper, Scissors, or quit: ","magenta", "input")
            if user_choice == "classic":
                player2=random.choice(RPS)
            else:
                os.system("cls")
                player2=colored_text(f"{p2_name} choose Rock, Paper, Scissors, or quit: ","magenta", "input")
                os.system("cls")
                if (player2=="rock" and user == "scissors")or(player2 == "scissors" and user == "paper") or (player2 == "paper" and user == "rock"):
                        colored_text(f"{p2_name} chose {player2} and you chose {user}","green","print")
                        colored_text("You Lost","yellow","print")
                        score3 -= 1
                        print (score3)
                elif score3 == 7:
                    colored_text("You won!","magenta","print")
                    while True:
                        user_homepage4 = (colored_text("Go back to homepage? y/n:","yellow","input"))
                        if user_homepage4=="y":
                            break
                        elif user_homepage4=="n":
                            colored_text("Goodbye!","red","print")
                            quit()
                        else:
                            colored_text("INVALID RESPONSE","red","print")
                    break

                elif (player2=="rock" and user == "paper")or(player2 == "paper" and user == "scissors") or (player2 == "scissors" and user == "rock"):
                    colored_text (f"{p2_name} chose {player2} and you chose {user}","green","print")
                    colored_text("You Won!","magenta","print")
                    score3 += 1
                    print (score3)
                elif player2 == user:
                    colored_text("Go Again","blue","print")
                elif user == "quit":
                    colored_text(f"score = {score3}","magenta","print")
                    colored_text("Bye!","cyan","print")
                    while True:
                        user_homepage1 = (colored_text("Go back to homepage? y/n:","yellow","input"))
                        if user_homepage1=="y":
                            break
                        elif user_homepage1=="n":
                            colored_text("Goodbye!","red","print")
                            quit()
                        else:
                            colored_text("INVALID RESPONSE","red","print")
                    break
                else:
                    colored_text("INVALID RESPONSE","red","print")
    elif user_choice=="rock paper scissors gun":
        colored_text("Welcome to Rock, Paper, Scissors, Gun!","cyan","print")
        while True:
            computer = random.choice(RPSG)
            user_response = (colored_text("Choose Rock, Paper, Scissors, Gun or quit: ","white","input"))
            if (computer=="rock" and user_response == "scissors")or(computer == "scissors" and user_response == "paper") or (computer == "paper" and user_response == "rock") or (computer == "gun" and user_response == "paper") or (computer == "gun" and user_response == "scissors") or (computer == "rock" and user_response == "gun"):
                colored_text(f"The computer chose {computer} and you chose {user_response}","green","print")
                colored_text("You Lost","yellow","print")
                score -= 1
                print (score)
            elif (computer=="rock" and user_response == "paper")or(computer == "paper" and user_response == "scissors") or (computer == "scissors" and user_response == "rock") or (computer == "paper" and user_response == "gun") or (computer == "scissors" and user_response == "gun") or (computer == "gun" and user_response == "rock"):
                colored_text (f"The computer chose {computer} and you chose {user_response}","green","print")
                colored_text("You Won!","magenta","print")
                score += 1
                print (score)
            elif score == 8:
                colored_text("You Won!","white","print")
                while True:
                    user_homepage1 = (colored_text("Go back to homepage? y/n:","yellow","input"))
                    if user_homepage1=="y":
                        break
                    elif user_homepage1=="n":
                        colored_text("Goodbye!","red","print")
                        quit()
                    else:
                        colored_text("INVALID RESPONSE","red","print")
                break
            elif computer == user_response:
                colored_text("Go Again","blue","print")
            elif user_response == "quit":
                colored_text(f"score = {score}","magenta","print")
                colored_text("Bye!","cyan","print")
                while True:
                    user_homepage = (colored_text("Go back to homepage? y/n:","yellow","input"))
                    if user_homepage=="y":
                        break
                    elif user_homepage=="n":
                        colored_text("Goodbye!","red","print")
                        quit()
                    else:
                        colored_text("INVALID RESPONSE","red","print")
                break
            else:
                colored_text("INVALID RESPONSE","red","print")
    elif user_choice== "magic 8 ball":
         while True:
            random_color=random.choice(["red","green","yellow","blue","magenta","white","cyan"])
            question=colored_text("Ask Magic 8 Ball a Question or quit:","white","input")
            random_response = random.choice(["Of course!","Definetly Not!","Maybe!","Ask me later!","No way", "Come back another time"])
            if question=="quit":
                while True:
                    user_homepage2 = (colored_text("Go back to homepage? y/n:","yellow","input"))
                    if user_homepage2=="y":
                        break
                    elif user_homepage2=="n":
                        colored_text("Goodbye!","red","print")
                        quit()
                    else:
                        colored_text("INVALID RESPONSE","red","print")
                break
            colored_text(random_response,random_color,"print")
    else:
        colored_text("INVALID RESPONSE","red","print")
