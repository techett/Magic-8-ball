###############################################
#
#   Created with care by C.T.
#   https://github.com/techett
#
###############################################

import random

version = 'Build v1'
author = 'https://github.com/techett'
title = "Magical 8 Ball Questions"
menu = "Press 1 for asking a question\nPress 2 to quit\n"
error_wrong_input = "That's not an appropiate response. Try again."

def question_menu():
    while True:
        try:
            menu_answer = int(input(menu))
            break
        except ValueError:
            print(error_wrong_input)
        
    if menu_answer == 1:
        question_ask()
    elif menu_answer == 2:
        quit()
    else:
        print(error_wrong_input)
        question_menu()
        
def another_question_menu():
    another_question = ["\nWould you like another question?\n",
                            "\nHow about another question?\n",
                            "\nGot another question?\n"]
    print(random.choice(another_question))
    
    while True:
        try:
            another_question_answer = int(input(menu))
            break
        except ValueError:
            print(error_wrong_input)
    
    if another_question_answer == 1:
        question_ask()
    elif another_question_answer == 2:
        print("Good bye!")
        quit()
    else:
        print(error_wrong_input)
        another_question_menu()
        
def question_ask():
    ask_the_user = ["\nWhat would you like to know?\n",
                    "\nWhat's your heart's desire?\n",
                    "\nA question for an answer.\n"]
    input(random.choice(ask_the_user))
    response()

def response():
    question_answer_list = ["Ask again later.", 
                            "Yes.", 
                            "I don't think so.", 
                            "For sure!", 
                            "My sources say no.", 
                            "Don't count on it.", 
                            "How about not?", 
                            "YES YES YES!!!", 
                            "Don't hold your breath."]
    question_answer = random.choice(question_answer_list)
    print(question_answer)
    another_question_menu()
    
def main():
    print("Welcome to " + title + ": " + version + "\nCreated by: " + author)
    question_menu()

main()