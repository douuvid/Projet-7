from itertools import combinations
import time



#Dans la deuxime boucle for il faudrait savoir combien de cmbinaison possible avec le big o
#et une fois qu'on a le nombre de combinaison on aura le nombre 

# il faut connaitre le nombre de combinaison en fonction des combinaiso  avec le big o
#dans quelle mesure elle, influenceren fonction des action (des entrees)
# look sur tous les algo
#la compexite big O = 2^N (n = nb d'action)


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