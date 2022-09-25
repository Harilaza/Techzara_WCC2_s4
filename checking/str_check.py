import re


def easy_answer_str(val, answer):
    valeurs = re.split('\s', val)
    for valeur in valeurs:
        if valeur not in answer:
            return "Non, ce n'est pas la bonne réponse" \
                   " \nDommage, vous avez echoué à la dernière question, la prochaine fois peut être"
        elif valeurs.count(valeur) > 1:
            return "La répétition des mots est inacceptable, la prochaine fois verifier bien"
    return 0


def medium_answer_str(response, answer):
    response_blank = re.sub('\s', '', response)
    response_specs = re.sub('[a-zA-Z\s]', '', response)
    if response_blank == '':
        return "les champs vides ne sont pas autorisés, repondez mieux la prochaine fois"
    elif response_specs != "":
        return "{} ne sont pas des chaines de caractère \n La prochaine fois verifier bien".format(response_specs)
    elif response == answer:
        return 0
    else:
        return "Non, ce n'est pas la bonne réponse" \
               " \nDommage, vous avez echoué à la dernière question, la prochaine fois peut être"


def hard_answer_str(response, answer):
    response_blank = re.sub('\s', '', response)
    response_specs = re.sub('[a-zA-Z\s]', '', response)
    if response_blank == '':
        return "les champs vides ne sont pas autorisés, repondez mieux la prochaine fois"
    elif response_specs != "":
        return "{} ne sont pas des chaines de caractère \n La prochaine fois verifier bien".format(response_specs)
    elif response == answer:
        return 0
    else:
        return "Non, ce n'est pas la bonne réponse" \
               " \nDommage, vous avez echoué à la dernière question, la prochaine fois peut être"
