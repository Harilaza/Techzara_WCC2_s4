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
    elif number:
        print("Il n'y a pas d'option valide pour ce choix")
    elif answer_number:
        for i in range(len(answer_number)):
            if answer_number.count(answer_number[i]) > 1:
                print("Ne pas mettre la même réponse deux fois la prochaine fois")
                break
            else:
                return answer_number



# verify if the answer is true or not
def verify_multiple_answer(answer, index, mode):
    a = 0
    if len(answer) > len(mode[index]["response"]):
        print("quelques réponse en trop")
        return 1
    elif len(answer) < len(mode[index]["response"]):
        print("Réponse manquante, réessayer une prochaine fois")
        return 1
    else:
        for i in range(len(answer)):
            if int(answer[i]) - 1 in mode[index]["response"]:
                a = a + 1
            else:
                a = 0
        if a == len(answer):
            print("Bonne réponse")
            return 0
        else:
            print("Vous avez fait une erreur, faites mieux la prochaine fois")
            return 1
