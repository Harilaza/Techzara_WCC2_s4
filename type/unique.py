from random import randrange
from checking.unique_check import verify_player_input, verify_unique_answer
from init.var_init import indices


def unique_run(mode):
    long = len(mode)
    index = randrange(long)
    print("\n\n\033[1;4m"+'Etape 2: '+"\033[0m Quiz à choix unique")
    print("\033[32m" + 'Taper : "quiz -i" pour avoir une indice' + "\033[0m")
    print("Question: ",mode[index]["question"])
    for x in range(len(mode[index]["suggestion"])):
        print(x+1, "- ", mode[index]["suggestion"][x])
    answer = input("votre réponse: ")
    if answer in indices:
        print(mode[index]["clues"])
        answer_after_clues = input("Votre reponse: ")
        if verif_clues(answer_after_clues, index, mode) == 1:
            return 1
        else:
            return 0

    else:
        if verif_clues(answer, index, mode) == 1:
            return 1
        else:
            return 0


def verif_clues(answer, index, mode):
    answer_verified = verify_player_input(answer)
    if answer_verified:
        if verify_unique_answer(answer_verified, index, mode) == 1:
            return 1
        else:
            return 0
    else:
        return 1