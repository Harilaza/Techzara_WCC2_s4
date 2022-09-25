import re


def check_int(val, answer):
    try:
        valeur = float(val)
        if valeur == answer:
            return "equal"
        else:
            return "Non, ce n'est pas la bonne réponse, faites mieux la prochaine fois."
    except:
        valeur = re.sub('[0-9]', '', val)
        return " '{}' n'est pas considérer comme étant un chiffre ou un nombre valable ." \
               "\n Vous ferez mieux la prochaine fois".format(valeur)
