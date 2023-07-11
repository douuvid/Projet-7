


## Sur ses 3 action il y a 3 combi et 50 e de bud
## Commencer par la 1er ligne
# Ac 1 + 2
# Ac 2
# Ac 3
from itertools import combinations


actions =[
  {"name":"Action-1" ,"cost" : 20, "benefice" : 5, "quantité":1 },
  {"name":"Action-2" ,"cost" : 30, "benefice" : 10, "quantité":1 }, 
  {"name":"Action-3" ,"cost" : 50,"benefice" : 15, "quantité":1 },
  {"name":"Action-4" ,"cost" : 7,"benefice" : 20, "quantité":1 },
  {"name":"Action-5" ,"cost" : 60,"benefice" : 17, "quantité":1 },
  
    
]

budget = 50 ###


def brute_force(actions, budget):
    if not actions:
        return None

    all_combinations = []
    best_combination = None
    best_benefit = 0
    ## il faudrait savoir combien de budget il nous reste 
    

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action['cost'] for action in combination)
            total_benefit = sum(action['benefice'] for action in combination)
            if total_cost <= budget:
                all_combinations.append(combination)
                if total_benefit > best_benefit:
                    best_combination = combination
                    best_benefit = total_benefit

    return all_combinations, best_combination, best_benefit


# all_combinations, best_combination, best_benefit = brute_force(actions, budget)

# print(f"Nombre de combinaisons possibles : {len(all_combinations)}")
# print("Toutes les combinaisons possibles :")
# for i, combination in enumerate(all_combinations, 1):
#     print(f"Combinaison {i} : {combination}")
#     print("Répartition des actions :")
#     total_cost = sum(action['cost'] for action in combination)
#     for action in combination:
#         action_budget_percentage = (action['cost'] / total_cost) * 100
#         print(f"{action['name']}: {action_budget_percentage:.2f}% du budget de : {budget}, euros")
#     print()



def print_best_combination(best_combination, best_benefit, budget, all_combinations):
    if best_combination:
        best_combination_index = all_combinations.index(best_combination) + 1
        print(f"Meilleure combinaison avec un budget de {budget} :")
        print(f"Combinaison {best_combination_index} :", best_combination)
        print("Composition de la combinaison :", end=" ")
        for action in best_combination:
            print(action['name'], end=" ")
        print()
        print(f"Bénéfice total : {best_benefit}")
        print("Répartition des actions :")
        total_cost = sum(action['cost'] for action in best_combination)
        for action in best_combination:
            action_budget_percentage = (action['cost'] / total_cost) * 100
            print(f"{action['name']}: {action_budget_percentage:.2f}% du budget de : {budget} euros")
    else:
        print("\nAucune combinaison valide avec un budget de", budget, ".")
        
        
       
def budget_restant(actions, best_combination, budget):
    if not best_combination:
        return 0

    budget_utilise = sum(action['cost'] for action in best_combination)
    budget_restant = budget - budget_utilise

    return budget_restant

        
        
        

     
all_combinations, best_combination, best_benefit = brute_force(actions, budget)
print(f"Nombre de combinaisons possibles : {len(all_combinations)}")
print_best_combination(best_combination, best_benefit, budget, all_combinations)

budget_restants = budget_restant(actions, best_combination, budget)
print(f"Montant restant dans le budget : {budget_restants} euros")





