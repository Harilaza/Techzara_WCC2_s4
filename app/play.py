#ALL IMPORTATION NEEDED FOR THE APP

from checking.check import contain_blank as blank
from type.multiple import multiple_run
from type.unique import unique_run
from type.int import int_run
from type.str import str_run
from app.helper import quiz_helper as helper
from answer.multiple_answer import multiple_answer_easy as me, multiple_answer_medium as mm, multiple_answer_hard as mh
from answer.unique_answer import unique_answer_easy as u_easy, unique_answer_medium as u_medium, \
    unique_answer_hard as u_hard
from answer.int_answer import easy_list_int as eli, medium_list_int as mli, hard_list_int as hli
from answer.str_answer import easy_list_str as els, medium_list_str as mls, hard_list_str as hls
from schemas.shemas import show_win


# Function which start the game
def starter():
    print("CHAMPION QUIZ")
    print("1- Lancer\n"
          "2- Aide\n"
          "3- Quitter")
    choice = input("Votre choix:")
    starter_choice(choice) # Checking the choice of the player


# The interface to print all mode
def mode_selector_interface():
    print("\nMode de jeu:")
    print("1- Facile\n"
          "2- Moyen\n"
          "3- Difficile")
    select = input("choisissez votre mode de jeu: ") # taking the player choice typing in the keyboard
    mode_selector(select) #launching the game


#Starting the game with the choice of player
def mode_selector(mode):
    if blank(mode): #check if the response of the choice is blank
        print("Le champ vide n'est pas accepté")
    try:
        mode = int(mode)
        if mode == 1:       # easy mode : launching the step
            if multiple_run(me) == 1:   # multiple answer
                starter()           # return to first page if player lose
            else:
                if unique_run(u_easy) == 1:  # launching next step : unique answer
                    starter()
                else:
                    if int_run(eli) == 1:   # launching next step : int answer
                        starter()
                    else:
                        if str_run(els, mode) == 1: # launching last step : chars answer
                            starter()
                        else:
                            show_win()
                            print("Bravo vous avez réussi le mode Facile")
        elif mode == 2:     #launching new level : medium if player want a medium level
            if multiple_run(mm) == 1:
                starter()
            else:
                if unique_run(u_medium) == 1:
                    starter()
                else:
                    if int_run(mli) == 1:
                        starter()
                    else:
                        if str_run(mls, mode) == 1:
                            starter()
                        else:
                            show_win()
                            print("Vous avez réussi le niveu moyen") # winning the level
        elif mode == 3:         # launching hard level if player wants high level
            if multiple_run(mh) == 1:
                starter()
            else:
                if unique_run(u_hard) == 1:
                    starter()
                else:
                    if int_run(hli) == 1:
                        starter()
                    else:
                        if str_run(hls, mode) == 1:
                            starter()
                        else:
                            show_win()
                            print("Vous avez réussi le niveu difficile")
        else:
            print("il n'y pas d'option valide pour ce choix.") # this is out of range
            print("choisissez entre 1, 2 ou 3")
            mode_selector_interface()
    except:     # the player enters inappropriate value
        print("La présence de chaine de caractère et caractère spéciaux n'est pas autorisé")
        mode_selector_interface()

# function to quit the application
def quiz_quit():
    print("Good-Bye")

# function to access to the helper
def quiz_helper():
    if helper() == 0:
        starter()
    else:
        quiz_quit()

# checking if the player enters a value which is accepted by the application
def starter_choice(choice):
    if blank(choice):
        print("une réponse vide n'est pas accepté")
        starter()
    try:
        choice = int(choice)
        if choice == 1:
            mode_selector_interface()
        elif choice == 2:
            quiz_helper()
        elif choice == 3:
            quiz_quit()
        else:
            print("il n'y pas d'option valide pour ce choix.")
            print("choisissez entre 1, 2 ou 3")
            starter()
    except:
        print("La présence de chaine de caractère et caractère spéciaux n'est pas autorisé")
        starter()
