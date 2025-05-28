import random                                                                                                                       #import random

name = input("What is your name?")                                                                                                  #set variable name to user name response
print (f"Good Luck {name}!")                                                                                                        #display message good luck, user name response
words = ["computer", "science", "programming","python","logic","boardgame","condition"]                                             #create a list with the following: computer, science, programming, python, logic, boardgame, condition
games = 0                                                                                                                           #games is 0
win_score = 0                                                                                                                       #win score is 0
while True:                                                                                                                         #forever loop
    word = random.choice(words)                                                                                                     #set variable word equal to random selection from words
    display = list(word)                                                                                                            #set display to the list of word
    random.shuffle(display)                                                                                                         #scramble display list
    display = ''.join(display)                                                                                                      #join list display and set it back to list display
    turns = 5                                                                                                                       #set turns to 5

    while turns>0:                                                                                                                  #While turns is greater than 0
        guess = input(f"{display}, enter the real word:")                                                                           #set guess equal to input; unscramble display, enter real word
        if guess==word:                                                                                                             #if guess equals word
            print ("You got it!")                                                                                                   #display message you got it
            win_score+=1                                                                                                            #add 1 point to win
            break                                                                                                                   #exit forever loop

        while True:                                                                                                                 #forever loop
            scramble = input ("You did not get the word. Yould you like to rescramble? Enter yes or no:")                           #set scramble equal to input; you did not get the word. Would you like to rescramble? Enter yes or no
            if scramble == "no":                                                                                                    #if scramble equals no
                break                                                                                                               #exit forever loop
            elif scramble == "yes":                                                                                                 #if scramble equals yes
                display = list(word)                                                                                                #set display equal to the list of words
                random.shuffle(display)                                                                                             #scramble display list
                display = ''.join(display)                                                                                          #join list display and set it back to list display
                break                                                                                                               #exit forever loop
            else:                                                                                                                   #else
                print ("Invalid Response")                                                                                          #display message invalid 
        turns -=1                                                                                                                   #minus 1 point from turn
    print (f"The word was {word}")                                                                                                  #display message the word was, word
    games +=1                                                                                                                       #add 1 point to game
    while True:                                                                                                                     #forever loop
        play_again = input(f"{name}, you have won {win_score} out of {games} games. Would you like to play again? yes or no:")      #set play again equal to input, name, you have won, win, out of games, gmaes. Would you like to play again? yes or no.
        if play_again=="no":                                                                                                        #if play again equals no
            exit                                                                                                                    #exit code
        elif play_again=="yes":                                                                                                     #if play again equals yes
            break                                                                                                                   #exit forever loop
        else:                                                                                                                       #else
            print ("Invalid Response. Limit to yes or no")                                                                          #display message Invalid Response. Limit to yes or no
    
    
        
    
