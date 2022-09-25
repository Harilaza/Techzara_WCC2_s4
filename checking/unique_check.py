import re
from checking.check import contain_blank as blank

# verify the input that the player give
def verify_player_input(player_answer):
    str_input = re.findall("[a-zA-Z]", player_answer)
    answer_number = re.findall("[1-4]", player_answer)
    number = re.findall("[05-9]", player_answer)
    if blank(player_answer):
        print("Un champ vide n'est pas accépté")
    elif str_input:
        print("ne pas remplir avec des chaines de caractères")
    elif answer_number:
        if len(answer_number) > 1:
            print("Une seule réponse est autorisée")
        else:
            return answer_number
    elif number:
        print("Il n'y a pas d'option valide pour ce choix")


# verify if the answer is true or not
def verify_unique_answer(answer, index, mode):
    if int(answer[0]) == int(mode[index]["answer"]):
        print("Bonne réponse")
        return 0
    else:
        print("Mauvaise réponse, réessayer plus tard")
        return 1
