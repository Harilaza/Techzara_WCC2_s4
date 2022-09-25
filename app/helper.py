from schemas.shemas import show_help
def quiz_helper():
    show_help()
    print("* \033[1;4m"+'REGLES'+"\033[0m\n"
          "\t- Le jeu se divise en 4 étape consécutif:\n"
          "\t\t. Quiz à choix multiple.\n"
          "\t\t. Quiz à choix unique.\n"
          "\t\t. Quiz avec réponse numérique.\n"
          "\t\t. Quiz avec réponse alphabétique précise\n"
          "\t- Tout erreur rammenera à l'écran de démarrage.\n"
          "* \033[1;4m"+'ERREUR'+"\033[0m\n"
          "\t- Pour chaque étape du jeu, un champ vide sera considéré comme une erreur.\n"
          "\t- Pour la 1ère étape:\n"
          "\t\t. Ne pas donner toute les réponse est considéré comme une erreur.\n"
          "\t- Pour les deux premières étapes: \n"
          "\t\t. Rédondance de réponse est considéré comme une erreur.\n"
          "\t\t. Mettre plus de réponse que prévue est considéré comme étant une erreur.\n"
          "\t- Pour les 3 premières étapes:\n"
          "\t\t. Chaine de caractère et caractère spéciaux seront considéré comme une erreur.\n"
          "* \033[1;4m"+'ASTUCES'+"\033[0m\n"
          "\t- Pour la dernière étape:\n"
          "\t\t. La réponse n'est pas sensible à la casse.\n"
          "\t Pour chaque questions et étapes, un indice leurs est atttribué.\n"
          "\t Pour y accéder taper la commande \033[2;7;3m"+'Quiz --indice'+"\033[m ou \033[2;7;3m"+'quiz --indice'+"\033[m "
            "ou \033[2;7;3m"+'Quiz -i'+"\033[m ou \033[2;7;3m"+'quiz -i'+"\033[m "
           "dans les champs des réponses")
    print("\033[1;4m"+'DEROULEMENT'+"\033[0m")
    print("** Ecran de Démarrage: \n"
          "\t- Choisir entre les trois options données: soit 1, 2 ou 3.\n"
          "\t\t \033[7m"+' 1 '+"\033[0m pour lancer le jeu et attérir sur l'écran de séléction de mode de jeu.\n"
          "\t\t \033[46;30m"+' 2 '+"\033[0m pour ouvrir le menu d'aide.\n"
          "\t\t \033[41;30m"+' 3 '+"\033[0m pour quitter le jeu")
    print("** Ecran de Selection de mode de jeu:\n"
          "\t- Il y trois mode de jeu:\n"
          "\t\t \033[7m"+' 1 '+"\033[0m pour lancer le jeu en mode facile.\n"
          "\t\t \033[46;30m"+' 2 '+"\033[0m pour lancer le jeu en mode normale.\n"
          "\t\t \033[41;30m"+' 3 '+"\033[0m pour lancer le jeu en mode difficile\n")
    select = input("Voulez vous retourner à l'interface de démarrage ? (o/n): ")
    if select == 'o' or select == 'O':
        return 0
    else:
        return 1