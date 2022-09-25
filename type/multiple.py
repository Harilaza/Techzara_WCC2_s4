from random import randrange
from checking.multiple_check import verify_player_input, verify_multiple_answer
from init.var_init import indices


# interface when player start a new game
def multiple_run(mode):
    long = len(mode)
    index = randrange(long)
    print("\n\n\033[1;4m"+'Etape 1:'+"\033[0m quiz à choix multiples \033[31m"+'(N.B séparé vos réponses par des éspaces)'+"\033[0m")
    print("\033[32m"+'Taper : "quiz -i" pour avoir une indice'+"\033[0m") # proposed to the player if he needs a clues
    print("Question: ", mode[index]["question"])
    for x in range(len(mode[index]["answer"])):
        print(x + 1, "-", mode[index]["answer"][x])
    answer = input("Votre reponse: ") # taking the player response
    if answer in indices:
        print("indice : ", mode[index]["clues"])
        answer_after_clues = input("Votre reponse: ")
        if verif_clues(answer_after_clues, index, mode) == 1:
            return 1
        else:
            return 0

    else:
        if verif_clues(answer, index, mode) == 1: # verify if the command is appropriate
            return 1
        else:
            return 0

# function which verify the command
def verif_clues(answer, index, mode):
    answer_verified = verify_player_input(answer)
    if answer_verified:
        if verify_multiple_answer(answer_verified, index, mode) == 1:
            return 1
        else:
            return 0
    else:
        return 1