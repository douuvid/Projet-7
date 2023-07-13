from itertools import combinations

actions =[
  {"name":"Action-1" ,"cost" : 20, "benefice" : 5 },
  {"name":"Action-2" ,"cost" : 30, "benefice" : 10 }, 
  {"name":"Action-3" ,"cost" : 50,"benefice" : 15 },
  {"name":"Action-4" ,"cost" : 70,"benefice" : 20 },
  {"name":"Action-5" ,"cost" : 60,"benefice" : 17 },
  {"name":"Action-6" ,"cost" : 80,"benefice" : 25 },
  {"name":"Action-7" ,"cost" : 22,"benefice" : 7 },
  {"name":"Action-8" ,"cost" : 26,"benefice" : 11 },
  {"name":"Action-9" ,"cost" : 48,"benefice" : 13 },
  {"name":"Action-10" ,"cost" : 34,"benefice" : 27 },
  {"name":"Action-11" ,"cost" : 42,"benefice" : 17 },
  {"name":"Action-12" ,"cost" : 110, "benefice" : 9 },
  {"name":"Action-13" ,"cost" : 38, "benefice" : 23 },
  {"name":"Action-14" ,"cost" : 14,"benefice" : 1 },
  {"name":"Action-15" ,"cost" : 18,"benefice" : 3 },
  {"name":"Action-16" ,"cost" : 8,"benefice" : 8 },
  {"name":"Action-17" ,"cost" : 4,"benefice" : 12 },
  {"name":"Action-18" ,"cost" : 10,"benefice" : 14 },
  {"name":"Action-19" ,"cost" : 24,"benefice" : 21 },
  {"name":"Action-20" , "cost" : 114,"benefice" : 18 }
    
]

budget = 200

total = 0
benefiii =0
for action in actions:
    total += action["cost"]
    benefiii += action["benefice"]
    

print( f"Le cout de toute les actions represente : {total}")
print(f"La valeur  de tous les benef represente : {benefiii}")


"""
Approches utilisées:

Le code utilise une approche dynamique pour trouver la meilleure combinaison.
Il crée une matrice dp de dimensions (n+1) x (budget+1), où n est le nombre d'actions. 
La valeur dp[i][j] représente le bénéfice maximal atteignable avec les i premières actions et un budget de j.


Le code parcourt ensuite cette matrice pour remplir les valeurs de manière itérative. 
Pour chaque action, il compare deux cas : soit l'action est exclue, auquel cas le bénéfice 
reste le même que pour les i-1 premières actions, soit l'action est incluse, auquel cas
le bénéfice est augmenté du bénéfice de cette action et du bénéfice maximal atteignable 
avec les i-1 premières actions et un budget réduit de son coût.

Une fois que la matrice dp est remplie, le code détermine le bénéfice maximal 
atteignable et les actions correspondantes en remontant dans la matrice.
Il construit la meilleure combinaison en ajoutant les actions qui ont contribué 
au bénéfice maximal, et calcule également le budget restant.

Ensuite, le code utilise une approche de force brute pour trouver toutes
les combinaisons possibles d'actions et calcule leur coût total et leur 
bénéfice total. Il génère une liste de tuples contenant chaque combinaison,
son coût total et son bénéfice total. Cette approche de force brute peut être
coûteuse en termes de temps de calcul, en particulier lorsque le nombre d'actions est élevé.

Enfin, le code imprime la meilleure combinaison trouvée avec le budget donné,
ainsi que le bénéfice total et le budget restant. Il affiche également le nombre 
total de combinaisons possibles (commenté dans le code), ainsi que toutes les
combinaisons possibles avec leur coût total, leur bénéfice total et la répartition des actions.
    """
    
    
########
def find_best_combination(actions, budget):
    n = len(actions)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if actions[i - 1]["cost"] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - actions[i - 1]["cost"]] + actions[i - 1]["benefice"])

    best_benefit = dp[n][budget]
    remaining_budget = budget
    best_combination = []

    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            best_combination.append(actions[i - 1])
            remaining_budget -= actions[i - 1]["cost"]
            j -= actions[i - 1]["cost"]
        i -= 1

    return best_combination, best_benefit, remaining_budget


def brute_force(actions, budget):
    if not isinstance(actions, list):
        return "Erreur : le paramètre 'actions' doit être une liste"

    if not actions:
        return None

   #all_combinations = []
    best_combination = None
    nb_combi = 0

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action["cost"] for action in combination)
            nb_combi += 1
            total_benefit = sum(action["benefice"] for action in combination)
            if total_cost <= budget and (best_combination is None or  total_benefit >= best_combination [2]):
                best_combination = (combination, total_cost, total_benefit,nb_combi)
                #all_combinations.append((combination, total_cost, total_benefit))

    return best_combination, nb_combi



#best_combination, best_benefit, remaining_budget = find_best_combination(actions, budget)

# print("Meilleure combinaison avec un budget de", budget, ":")
# for action in best_combination:
#     print(action["name"], end=" ")
# print()
# print("Bénéfice total :", best_benefit)
# print("Montant restant dans le budget :", remaining_budget)

best_combination, nb_combi = brute_force(actions, budget)
print(f"Nombre de combinaisons possibles : {nb_combi}")

print("ici")

print(f"La meileur combiansaison est la numeros {best_combination[3]}:  \n {best_combination[0]}")
# print("Toutes les combinaisons possibles :")
# for i, (combination, total_cost, total_benefit) in enumerate(all_combinations, 1):
#     print(f"Combinaison {i} : {combination}")
#     print(f"Coût total : {total_cost}")
#     print(f"Bénéfice total : {total_benefit}")
#     print("Répartition des actions :")
#     for action in combination:
#         action_budget_percentage = (action['cost'] / total_cost) * 100
#         print(f"{action['name']}: {action_budget_percentage:.2f}% du budget de : {total_cost} euros")
#     print()
