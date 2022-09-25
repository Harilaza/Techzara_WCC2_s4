from random import randrange
from init.var_init import init
from checking.str_check import easy_answer_str, medium_answer_str, hard_answer_str
from init.var_init import indices


def str_run(liste, mode):
    index = randrange(4)
    var = init(liste[index]["question"], liste[index]["answer"], liste[index]["clues"])
    print("\n\n\033[1;4m"+'Etape 4:'+"\033[0m Quiz a valeur Alphabétique:")
    print("\033[32m" + 'Taper : "quiz -i" pour avoir une indice' + "\033[0m")
    print(var["ask"])
    key = input("la réponse est : ")
    if key in indices:
        print(var["clues"])
        response = input("donc la reponse est : ")
        if mode == 1:
            check = easy_answer_str(response.lower(), var["answer"])
            if check == 0:
                return 0
            else:
                print(check)
                return 1
        elif mode == 2:
            check = medium_answer_str(response.lower(), var["answer"])
            if check == 0:
                return 0
            else:
                print(check)
                return 1
        elif mode == 3:
            check = hard_answer_str(response.lower(), var["answer"])
            if check == 0:
                return 0
            else:
                print(check)
                return 1
    else:
        if mode == 1:
            check = easy_answer_str(key.lower().lower(), var["answer"])
            if check == 0:
                return 0
            else:
                print(check)
                return 1
        elif mode == 2:
            check = medium_answer_str(key.lower().lower(), var["answer"])
            if check == 0:
                return 0
            else:
                print(check)
                return 1
        elif mode == 3:
            check = hard_answer_str(key.lower().lower(), var["answer"])
            if check == 0:
                return 0
            else:
                print(check)
                return 1