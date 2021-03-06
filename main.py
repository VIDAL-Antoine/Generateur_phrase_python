# -*- coding: utf-8 -*-

import sentence
import dico

def getUserChoice(pnUpperBound : int):
    '''
    getUserChoice()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
    Cette fonction demande à l'utilisateur un entier représentant l'action qu'il souhaite effectuer.
    La fonction réalise différents tests pour s'assurer que la saisie est bien correcte.
    Elle vérifie que la saisie est bien un nombre et que celui-ci se situe dans les bornes appropriées.

    Entrées :
        pnUpperBound : l'entier maximal représentant la dernière action possible (vaut 5 par exemple s'il y a 5 actions possibles).

    Sorties :
        lEChoice : entier représentant l'action souhaitée.
    '''

    lEChoice = -1
    try:
        lEChoice = int(input(f'Veuillez choisir un nombre entre 0 et {pnUpperBound} : '))

    except ValueError:
        print(f'\nERREUR : la saisie n\'est pas un nombre.')

    else:
        if lEChoice < 0 or lEChoice > pnUpperBound:
            print(f'\nERREUR : Nombre hors portée.')

    return lEChoice

def main():
    '''
    main()

    Auteur : VIDAL Antoine
    Projet : Générateur de phrase

    Description :
    La fonction principale du programme. L'utilisateur doit saisir un nombre représentant son action désirée.
    Pour quitter, l'utilisateur doit saisir 0.

    Entrées :
        -

    Sorties :
        -
    '''

    lEChoice = -1 #Représente l'option choisie par l'utilisateur, réinitialisée à -1 après qu'une option soit effectuée

    print(f'Ouverture du dictionnaire...')
    dico.openDictionary()
    print(f'Ouverture terminée.')

    while(lEChoice != 0):
        lEChoice = -1

        print("\nBienvenue dans le générateur de phrases. Voici la liste des options disponibles :\n",
        "0 - Quitter",
        "1 - Afficher le dictionnaire",
        "2 - Générer une phrase automatique",
        "3 - Entrer une phrase et vérifier si elle est correcte",
        "4 - Ajouter un mot au dictionnaire",
        "5 - Retirer un mot au dictionnaire",
        "6 - Enregistrer les modifications faites au dictionnaire",
        sep = '\n'
        )

        #Vérifier que la saisie est bien un chiffre représentant une action possible
        lEChoice = getUserChoice(6)

        #Effectuer le choix de l'utilisateur

        #Affichage du dictionnaire
        if lEChoice == 1:
            dico.printDictionary()

        #Génération d'une phrase automatique
        elif lEChoice == 2:
            lsSentenceRandom = sentence.Sentence() #phrase créée pour générer une phrase aléatoire
            lsSentenceRandom.generateRandomSentence()
            print(f'\nLa phrase générée est la suivante :')
            lsSentenceRandom.printSentence()

        #Saisie d'une phrase et vérification de celle-ci
        elif lEChoice == 3:
            lwPhraseCheck = input("\nVeuillez saisir une phrase :\n") #phrase créée pour vérifier sa validité
            lwPhraseCheck = lwPhraseCheck.strip()
            lsSentence = sentence.Sentence() #Structure pour pouvoir différencier le sujet du verbe...

            if len(lwPhraseCheck) != 0:
                if(lsSentence.checkIsValidSentence(lwPhraseCheck)):
                    print(f'La phrase est bien valide.')
                else:
                    print(f'La phrase n\'est pas valide.')
            else:
                print("La phrase est vide. Veuillez saisir une phrase pour pouvoir la vérifier.")

        #Ajouter un mot au dictionnaire
        elif lEChoice == 4:

            #Rester dans le menu d'ajout tant que l'utilisateur le souhaite
            while(lEChoice != 0):
                lEChoice = -1

                print("\nSouhaitez-vous ajouter un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Ajouter un sujet",
                "2 - Ajouter un verbe",
                "3 - Ajouter un adverbe",
                sep = '\n'
                )

                #Vérifier que la saisie est bien un chiffre représentant une action possible
                lEChoice = getUserChoice(3)

                #Quitter le menu d'ajout
                if lEChoice == 0:
                    lEChoice = -1
                    break

                #Ajouter dans la liste adéquate
                if lEChoice == 1:
                    print(f'Sujets : {dico.gvSubjects}\n')
                    dico.addSubject()

                elif lEChoice == 2:
                    print(f'Verbes : {dico.gvVerbs}\n')
                    dico.addVerbAdverb(dico.gvVerbs)

                elif lEChoice == 3:
                    print(f'Adverbes : {dico.gvAdverbs}\n')
                    dico.addVerbAdverb(dico.gvAdverbs)

                #L'utilisateur a tapé une option non reconnue
                else:
                    pass

        #Retirer un mot du dictionnaire
        elif lEChoice == 5:

            #Rester dans le menu de retrait tant que l'utilisateur le souhaite
            while(lEChoice != 0):
                lEChoice = -1

                print("\nSouhaitez-vous retirer un sujet, un verbe ou un adverbe?\n",
                "0 - Annuler",
                "1 - Retirer un sujet",
                "2 - Retirer un verbe",
                "3 - Retirer un adverbe",
                sep = '\n'
                )

                #Vérifier que la saisie est bien un chiffre représentant une action possible
                lEChoice = getUserChoice(3)

                #Quitter le menu de retrait
                if lEChoice == 0:
                    lEChoice = -1
                    break

                #Retirer de la liste adéquate
                elif lEChoice == 1:
                    print(f'\nSujets : {dico.gvSubjects}\n')
                    dico.removeItem(dico.gvSubjects)

                elif lEChoice == 2:
                    print(f'\nVerbes : {dico.gvVerbs}\n')
                    dico.removeItem(dico.gvVerbs)

                elif lEChoice == 3:
                    print(f'\nAdverbes : {dico.gvAdverbs}\n')
                    dico.removeItem(dico.gvAdverbs)

                #L'utilisateur a tapé une option non reconnue
                else:
                    pass

        #Enregistrer les modifications faites au dictionnaire
        elif lEChoice == 6:
            dico.saveDictionary()
            print(f'Les modifications ont été enregistrées.')

        #L'utilisateur a tapé une option non reconnue
        else:
            pass

    print(f'\nMerci d\'avoir utilisé ce dictionnaire! Au revoir!')

if __name__ == "__main__":
    main()
