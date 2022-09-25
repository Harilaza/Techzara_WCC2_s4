from random import randrange
from checking.int_check import check_int
from init.var_init import init
from init.var_init import indices

# to run the question with the integer value
def int_run(liste):
    index = randrange(4) # taking random from the list of answer
    var = init(liste[index]["question"], liste[index]["answer"], liste[index]["clues"])
    print("\n\n\033[1;4m"+'Etape 3:'+"\033[0m Quiz a valeur numérique:")
    print("\033[32m" + 'Taper : "quiz -i" pour avoir une indice' + "\033[0m")
    print("Question: ", var["ask"]) # asking the question to the player
    key = input("la réponse est : ")
    if key in indices:
        print(var["clues"]) # showing the clues to the player
        response = input("donc la réponse est : ")
        check = check_int(response.lower(), var["answer"]) # checking the answer
        if check == "equal": # retrun 0 if true and 1 if false
            return 0
        else:
            print(check)
            return 1
    else:
        check = check_int(key.lower(), var["answer"])
        if check == "equal":
            return 0
        else:
            print(check)
            return 1