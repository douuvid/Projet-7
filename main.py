
import csv
import logging
import time

from brut_2 import action_plus_benef
from brute_force import brute_force
from optimized import optimized
from version_dynamique import calculer_taux_de_rendement_fichier_csv

logging.basicConfig(level=logging.DEBUG)
# log error pour les fichier corrompu et afficher le pb
# Qaund on sait pas si c'est une erreur ou pas mettre warning
# Raise exeption quand c'est mort et qu'il faut arrete le traitement et renvoyer un cas d'erreur
# Revoir les raise et les log
# Finir le glouton
# remettre au propre et mettre chaque algo par fichier

# verifie le calcule des
# remplacer les print par des logging


# https://www.programiz.com/python-programming/examples/elapsed-time
# Voir le temps sur force brut et glouton et comparer


actions = [
    {"name": "Action-1", "cost": 20, "percent_benefit": 5},
    {"name": "Action-2", "cost": 30, "percent_benefit": 10},
    {"name": "Action-3", "cost": 50, "percent_benefit": 15},
    {"name": "Action-4", "cost": 70, "percent_benefit": 20},
    {"name": "Action-5", "cost": 60, "percent_benefit": 17},
    {"name": "Action-6", "cost": 80, "percent_benefit": 25},
    {"name": "Action-7", "cost": 22, "percent_benefit": 7},
    {"name": "Action-8", "cost": 26, "percent_benefit": 11},
    {"name": "Action-9", "cost": 48, "percent_benefit": 13},
    {"name": "Action-10", "cost": 34, "percent_benefit": 27},
    {"name": "Action-11", "cost": 42, "percent_benefit": 17},
    {"name": "Action-12", "cost": 110, "percent_benefit": 9},
    {"name": "Action-13", "cost": 38, "percent_benefit": 23},
    {"name": "Action-14", "cost": 14, "percent_benefit": 1},
    {"name": "Action-15", "cost": 18, "percent_benefit": 3},
    {"name": "Action-16", "cost": 8, "percent_benefit": 8},
    {"name": "Action-17", "cost": 4, "percent_benefit": 12},
    {"name": "Action-18", "cost": 10, "percent_benefit": 14},
    {"name": "Action-19", "cost": 24, "percent_benefit": 21},
    {"name": "Action-20", "cost": 114, "percent_benefit": 18}
]


budget = 100
total = 0
benefiii = 0


name_file = 'dataset1'
position = 1
chemin_du_fichier = f'/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/{name_file}.csv'


if __name__ == "__main__":

    solution, nombre_combi = brute_force(actions, budget)
    logging.debug(f"La meilleur solution est {solution} ")
    logging.info("Recherche de la meileur  combinaison")
    logging.info("Recherche de la combinaison")
    logging.debug(
        f"La meilleur combinaison  est {[action['name'] for action in solution[0]]}")
    # Rajouter le benf
    logging.info("Recherche du nombre de combinaison ")
    logging.info("Recherche du nombre de combinaison ")
    logging.debug(f"Nombre de combinaisons possibles : {nombre_combi}")
    print("")

    start_time = time.time()
    print(brute_force(actions, budget))
    end_time = time.time()

    print("Time: ", end_time - start_time)

    # for action in actions:
    #     total += action["cost"]
    #     benefiii += round(action["cost"] *(action["percent_benefit"] / 100), 10)

    # print(f"Le coût de toutes les actions représente : {total} euro")
    # print(f"La valeur de tous les bénéfices représente : {round(benefiii,10)} euro")

    # print(f"pour le fichier {name_file}")
    # print("")
    # calculer_taux_de_rendement_fichier_csv(chemin_du_fichier)

    logging.info("On s'apprete a utiliser la programmation dynamque ")
    logging.info("On s'apprete a utiliser la programmation dynamque ")

    meilleure_combinaison, max_benefit = optimized(actions, budget)
    print(f"Meilleure combinaison d'actions optimisé  avec {budget}euros:")

    for action in meilleure_combinaison:
        print(action)
    print(f"Bénéfice maximal : {round(max_benefit,10 )}")

    print("")
    print("")
    # resultat=action_plus_benef(actions,budget)


# for action in actions:
#     total += action["cost"]
#     benefiii += round(action["cost"] * (action["percent_benefit"] / 100), 10)

#     print(f"Le coût de l'action {action['name']} est de {action['cost']} euro")
#     print(f"Le bénéfice de l'action {action['name']} est de {round(action['cost'] * (action['percent_benefit'] / 100), 10)} euro")
#     print()

# print(f"Le coût de toutes les actions représente : {total} euro")
# print(f"La valeur de tous les bénéfices représente : {round(benefiii,10)} euro")


# meilleure_combinaison, max_benefit = optimized.py(actions, budget)

# print("Meilleure combinaison d'actions :")
# for action in meilleure_combinaison:
#     print(action)
# print(f"Bénéfice maximal : {max_benefit}")

# name_file= 'dataset1'
# chemin_du_fichier = f'/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/{name_file}.csv'
# print(f"pour le fichier {name_file}")
# calculer_taux_de_rendement_fichier_csv(chemin_du_fichier)
