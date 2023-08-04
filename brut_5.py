from collections import defaultdict
##Faitmk,
import random
from itertools import product
from collections import Counter

actions = [
    {"name": "Axa", "cost": 20, "percent_benefit": 5},
    {"name": "BNP", "cost": 30, "percent_benefit": 10},
    {"name": "LVMH", "cost": 50, "percent_benefit": 15},
    {"name":"Action-6" ,"cost" : 80,"percent_benefit" : 2 },
  
  {"name":"Action-14" ,"cost" : 14,"percent_benefit" : 1 }
]

budget = 130

def generate_combinations(actions):
    if not actions:
        return []
    
    all_combinations = []
    for r in range(1, len(actions) + 1):
        all_combinations += list(product(actions, repeat=r))
    
    return all_combinations





def calculate_portfolio_combinations(all_combinations, budget):
    if not isinstance(all_combinations, list) or not isinstance(budget, (int, float)):
        return []
    
    portfolio_combinations = []
    total_cost_dict = {}
    
    for combination in all_combinations:
        total_cost = sum(action.get('cost', 0) for action in combination)
        if total_cost <= budget:
            portfolio_combinations.append(combination)
    
    return portfolio_combinations







def calculate_total_benefit(portfolio_combinations):
    if not isinstance(portfolio_combinations, list):
        raise ValueError("portfolio_combinations must be a list")
    
    if not portfolio_combinations:
        return None, 0
    
    best_combination = None
    best_benefit = 0
    
    for combination in portfolio_combinations:
        total_benefit = sum(action['percent_benefit'] for action in combination)
        
        if total_benefit > best_benefit:
            best_combination = combination
            best_benefit = total_benefit
    
    return best_combination, best_benefit

def calculate_action_distribution(best_combination):
    try:
        action_counts = defaultdict(int)
        for action in best_combination:
            action_counts[action['name']] += 1

        total_combinations = len(best_combination)
        action_distribution = {action_name: (count / total_combinations * 100, count) for action_name, count in action_counts.items()}

        return action_distribution

    except TypeError:
        return {}

# Générer toutes les combinaisons possibles avec répétition
all_combinations = generate_combinations(actions)

print(f"Nombre de combinaisons possibles : {len(all_combinations)}")

# Calculer les combinaisons valides pour le portefeuille
portfolio_combinations = calculate_portfolio_combinations(all_combinations, budget)

# Calculer la meilleure combinaison et le bénéfice total
best_combination, best_benefit = calculate_total_benefit(portfolio_combinations)

# Calculer la répartition des actions dans la meilleure combinaison
action_distribution = calculate_action_distribution(best_combination)

# Afficher la meilleure combinaison et le bénéfice total
if best_combination is not None:
    best_combination_index = portfolio_combinations.index(best_combination) + 1
    print(f"La meilleure combinaison est la numéro {best_combination_index}:")
    
    for i, action in enumerate(best_combination, 1):
        name = action['name']
        cost = action['cost']
        percent_benefit = action['percent_benefit']
        count = action_distribution[name][1]
        percentage = action_distribution[name][0]
        
        print(f"Action {i} - Nom: {name}, Coût: {cost}, Bénéfice: {percent_benefit}, "
              f"Quantité: {count}, Pourcentage dans le portfeuille : {percentage}%")
    
    print(f"Bénéfice total : {best_benefit}")
    
else:
    print("Aucune combinaison valide n'a été trouvée.")