from itertools import combinations
import csv
import logging


def brute_force(actions, budget):
    if not isinstance(actions, list):
        return "Erreur : le paramètre 'actions' doit être une liste"

    if not actions:
        return None

    best_combination = None
    nb_combi = 0

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action["cost"] for action in combination)
            total_benefit = sum(action["cost"] *  action["percent_benefit"] / 100 for action in combination)
            if total_cost <= budget:
                nb_combi += 1
                if best_combination is None or total_benefit >= best_combination[2]:
                    best_combination = (combination, total_cost, total_benefit, nb_combi)

    return  best_combination, nb_combi


"""

Voir la complexite de sum() et de combinaison


combinaison : Dans Python, le module itertools fournit
une fonction utile appelée combinations. Cette fonction 
permet de générer toutes les combinaisons possibles d'une 
séquence donnée en spécifiant la longueur de chaque combinaison.

L18 : Dans cette ligne, nous utilisons une expression de compréhension 
de liste pour obtenir une liste des coûts de chaque action dans la combinaison.
Ensuite, nous passons cette liste à la fonction sum() pour obtenir la somme totale des coûts.


L19:De manière similaire, nous utilisons une expression de compréhension de liste pour obtenir
une liste des bénéfices de chaque action dans la combinaison. Nous multiplions le coût de chaque 
action par son pourcentage de bénéfice, puis nous divisons par 100 pour obtenir la valeur réelle du bénéfice.
Ensuite, nous passons cette liste à la fonction sum() pour obtenir la somme totale des bénéfices.

Ces calculs nous permettent de déterminer si une combinaison est valide en fonction du budget donné,
et de comparer les différentes combinaisons pour trouver celle qui a le bénéfice le plus élevé tout 
en respectant le budget.




sum : Dans notre algorithme, nous utilisons la fonction sum() 
pour calculer la somme des coûts des actions et la somme des 
bénéfices des actions dans une combinaison donnée




Derniere partie 
Chercher les algo pour le probleme sac a dos (ne pas utiliser l'algo glouton)
Prend l'algo que j'ai le mieux compris +  verifie le temps + savoir l'explique 




Soution Programmation dynamique pour le problème du sac à dos :
La programmation dynamique consiste à diviser le problème en sous-problèmes plus petits,
de manière récursive, et à mémoriser les résultats de chaque sous-problème pour éviter de 
les recalculer à chaque fois. On construit généralement une matrice pour stocker les solutions
intermédiaires. Cette approche garantit la solution optimale pour le problème du sac à dos, 
mais peut être plus complexe à mettre en œuvre



"""





def taux_de_rendement(prix_achat, prix_vente):
    if prix_achat is not None and prix_vente is not None:
        prix_achat_float = float(prix_achat.replace(',', '.')) 
        prix_vente_float = float(prix_vente.replace(',', '.')) 

        if prix_achat_float > 0:
            rendement = ((prix_vente_float - prix_achat_float) / prix_achat_float) * 100
            if rendement >= 0:
                return f"Bon rendement chacal : {rendement}"
            else:
                return f"Vous avez subi une perte de {abs(rendement):.2f}%"
        else:
            return "Rendement impossible à calculer (prix d'achat nul)"
    else:
        return "Rendement impossible à calculer (données manquantes)"
    
    ##24 juillet 
    ## Donner coromp faire comme ci exite pas de scase vide 
    ## Mettre du log ==> si action  vide ou null printe ligne coromp
    ## https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos
    ## la cap du sac c'est le budget
    ##valeur ou poid = cout? a verifier 
    ## colone = budget entier donc arrondir 
    ## autant de ligne que d'actions
    ## imple l'algo wiki sur mon py
    
    
    
def programmation_dynamique(actions, budget):
    nombre_actions = len(actions)  # On compte le nombre total d'actions

    # On initialise un tableau pour stocker nos calculs intermédiaires.
    # Le tableau a (nombre_actions + 1) lignes et (budget + 1) colonnes.
    # On remplit le tableau avec des zéros.
    tableau = []
    for _ in range(nombre_actions + 1):
        tableau.append([0] * (budget + 1))

    # On parcourt le tableau ligne par ligne
    for i in range(1, nombre_actions + 1):
        for c in range(1, budget + 1):
            # Le coût de l'action actuelle est le coût de l'action à l'index (i - 1) dans la liste des actions
            cout_action_actuelle = actions[i - 1]["cost"]

            # Le bénéfice de l'action actuelle est le pourcentage de bénéfice de l'action à l'index (i - 1) dans la liste des actions,
            # multiplié par le coût de cette action
            benefice_action_actuelle = actions[i - 1]["cost"] * actions[i - 1]["percent_benefit"] / 100

            # Si le coût de l'action actuelle est inférieur ou égal à la capacité actuelle du sac à dos (c)
            if cout_action_actuelle <= c:
                # On peut choisir d'inclure l'action actuelle dans le sac à dos.
                # Si on l'inclut, le bénéfice total est le bénéfice de l'action actuelle, plus le bénéfice total qu'on peut obtenir
                # avec le reste de la capacité du sac à dos (c - cout_action_actuelle).
                # Si on n'inclut pas l'action actuelle, le bénéfice total est le même que le bénéfice total de la ligne précédente.
                tableau[i][c] = max(tableau[i - 1][c], tableau[i - 1][c - cout_action_actuelle] + benefice_action_actuelle)
            else:
                # Si le coût de l'action actuelle est supérieur à la capacité actuelle du sac à dos, on ne peut pas inclure l'action actuelle.
                # Donc, le bénéfice total est le même que le bénéfice total de la ligne précédente.
                tableau[i][c] = tableau[i - 1][c]

    # Maintenant, on retrouve la meilleure combinaison d'actions.
    meilleure_combinaison = []
    c = budget
    for i in range(nombre_actions, 0, -1):
        # Si le bénéfice total de la ligne actuelle est différent du bénéfice total de la ligne précédente,
        # cela signifie que l'action à l'index (i - 1) dans la liste des actions a été incluse dans la meilleure combinaison.
        if tableau[i][c] != tableau[i - 1][c]:
            meilleure_combinaison.append(actions[i - 1])
            c -= actions[i - 1]["cost"]

    return meilleure_combinaison, tableau[nombre_actions][budget]


    

def calculer_taux_de_rendement_fichier_csv(nom_fichier):
    with open(nom_fichier, newline='') as csvfile:
        # Spécifier manuellement les noms des colonnes avec fieldnames
        fieldnames = ['name', 'price', 'profit']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        # Ignorer la première ligne (en-tête) car nous l'avons spécifiée manuellement
        next(reader)
        total_achat_action = 0
        somme_total_action = 0  # Initialiser la somme totale à zéro

        for row in reader:
            nom_action = row['name']
            prix_achat = row["price"]
            prix_vente = row["profit"]
            resultat = taux_de_rendement(prix_achat, prix_vente)
            total_achat_action += 1  # Incrémenter le nombre total d'action
            if prix_achat and not prix_achat.isspace() and prix_achat != "0":
                
             # Faire quelque chose avec prix_achat...
                try:
                    somme_total_action += float(prix_achat.replace(',', '.'))  # Ajouter le prix d'achat à la somme totale
                except ValueError:
                    logging.error(f"Erreur : Impossible de convertir le prix d'achat de l'action {nom_action} en float.")
                    continue
            logging.info(f"Action : {nom_action}, Taux de rendement : {resultat}%")

        logging.info(f"Le nombre total d'actions est : {total_achat_action} action pour un montant total de {somme_total_action:.2f} euro")
        # print(f"Pour le fichier {name_file}")

# Exemple d'utilisation avec le fichier csv que vous avez fourni
# name_file= 'dataset1'
# chemin_du_fichier = f'/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/{name_file}.csv'
# calculer_taux_de_rendement_fichier_csv(chemin_du_fichier)


"""

    Conclusion

    Avec un calcule de une formule de taux de rendement 
    On peut voir des erreurs 
    Notamment qu'il y a des case nul qui on fait du profit wtf
    + taux rendement negatif
"""








