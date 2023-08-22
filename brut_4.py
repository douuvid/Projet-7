
from itertools import combinations

actions = [
    {"name": "Action-1", "cost": 20, "percent_benefit": 5, "quantité": 1},
    {"name": "Action-2", "cost": 30, "percent_benefit": 10, "quantité": 1},
    {"name": "Action-3", "cost": 50, "percent_benefit": 15, "quantité": 1},
    # {"name": "Action-4", "cost": 70, "percent_benefit": 20, "quantité": 1},
    # {"name": "Action-5", "cost": 60, "percent_benefit": 17, "quantité": 1},
]

budget = 22

def brute_force(actions, budget):
    if not isinstance(actions, list):
        return "Erreur : le paramètre 'actions' doit être une liste"

    if not actions:
        return None

    all_combinations = []
    best_combination = None
    best_benefit = 0
    remaining_budget = budget

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action["cost"] for action in combination)
            total_benefit = sum(action["percent_benefit"] for action in combination)
            budget_remaining = remaining_budget - total_cost
            if total_cost <= remaining_budget and total_benefit > best_benefit:
                all_combinations.append(combination)
                best_combination = combination
                best_benefit = total_benefit
                remaining_budget = budget_remaining

    return all_combinations, best_combination, best_benefit, remaining_budget

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

all_combinations, best_combination, best_benefit, budget_restants = brute_force(actions, budget)


while budget_restants > 0:
    actions.append({"name": f"Action-{len(actions)+1}", "cost": 1, "percent_benefit": 1, "quantité": 1})
    all_combinations, best_combination, best_benefit, budget_restants = brute_force(actions, budget)

print(f"Nombre de combinaisons possibles : {len(all_combinations)}")
print_best_combination(best_combination, best_benefit, budget, all_combinations)
print(f"Montant restant dans le budget : {budget_restants} euros")




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



 
       
"""
    L'objectif de la fonction 'budget_restant' est de 
    calculer le budget restant après avoir sélectionné 
    la meilleure combinaison d'actions à partir d'une liste 
    donnée d'actions et d'une contrainte de budget.
    """
def budget_restant(actions, best_combination, budget):
    if not best_combination:
        return 0

    if not isinstance(budget, (int, float)):
        raise ValueError("Budget must be a number")

    budget_utilise = sum(action['cost'] for action in best_combination)
    budget_restant = budget - budget_utilise

    return budget_restant

        
        
        

