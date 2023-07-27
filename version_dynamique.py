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

Soution Programmation dynamique pour le problème du sac à dos :
La programmation dynamique consiste à diviser le problème en sous-problèmes plus petits,
de manière récursive, et à mémoriser les résultats de chaque sous-problème pour éviter de 
les recalculer à chaque fois. On construit généralement une matrice pour stocker les solutions
intermédiaires. Cette approche garantit la solution optimale pour le problème du sac à dos, 
mais peut être plus complexe à mettre en œuvre



"""



#logging.basicConfig(level=logging.DEBUG)



def taux_de_rendement(prix_achat, prix_vente):
    logging.info('Début du calcul du rendement.')

    if prix_achat is not None and prix_vente is not None:
        logging.info('Les prix d\'achat et de vente sont fournis.')

        prix_achat_float = float(prix_achat.replace(',', '.')) 
        prix_vente_float = float(prix_vente.replace(',', '.')) 

        logging.info(f'Prix d\'achat converti en float: {prix_achat_float}, Prix de vente converti en float: {prix_vente_float}')

        if prix_achat_float > 0:
            rendement = ((prix_vente_float - prix_achat_float) / prix_achat_float) * 100

            logging.info(f'Rendement calculé: {rendement}')

            if rendement >= 0:
                logging.info('Rendement positif.')
                return f"Bon rendement chacal : {round(rendement)}🔥⬆️"
            else:
                logging.info('Rendement négatif.')
                return f"Vous avez subi une perte de {abs(rendement):.2f}% 🥶⬇️"
        else:
            logging.warning('Rendement impossible à calculer (prix d\'achat nul)')
            return "Rendement impossible à calculer (prix d'achat nul)"
    else:
        logging.warning('Rendement impossible à calculer (fichier corrompus)')
        return "Rendement impossible à calculer (fichier corrompus)"

    
    ##24 juillet 
  

    
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
            
            if prix_achat != "0":
                resultat = taux_de_rendement(prix_achat, prix_vente)
                print(f"Action : {nom_action}, Taux de rendement : {resultat}%")
            else:
                print(f"L'action {nom_action} a un prix d'achat de 0. Son taux de rendement n'est pas calculé.")
            total_achat_action += 1
            
            try:
                somme_total_action += float(prix_achat.replace(',', '.'))  # Ajouter le prix d'achat à la somme totale
            except ValueError:
                print(f"Erreur : Impossible de convertir le prix d'achat de l'action {nom_action} en float.")
                continue

        print(f"Le nombre total d'actions est : {total_achat_action} action pour un montant total de {somme_total_action:.2f} euro")
        # print(f"Pour le fichier {name_file}")




"""

    Conclusion

    Avec un calcule de une formule de taux de rendement 
    On peut voir des erreurs 
    Notamment qu'il y a des case nul qui on fait du profit wtf
    + taux rendement negatif
"""