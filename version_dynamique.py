from itertools import combinations

actions = [
    {"name": "Action-1", "cost": 20, "benefice": 5, "quantité": 1},
    {"name": "Action-2", "cost": 30, "benefice": 10, "quantité": 1},
    {"name": "Action-3", "cost": 50, "benefice": 15, "quantité": 1},
]

budget = 50

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

    all_combinations = []

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action["cost"] for action in combination)
            total_benefit = sum(action["benefice"] for action in combination)
            if total_cost <= budget:
                all_combinations.append((combination, total_cost, total_benefit))

    return all_combinations


best_combination, best_benefit, remaining_budget = find_best_combination(actions, budget)

print("Meilleure combinaison avec un budget de", budget, ":")
for action in best_combination:
    print(action["name"], end=" ")
print()
print("Bénéfice total :", best_benefit)
print("Montant restant dans le budget :", remaining_budget)

all_combinations = brute_force(actions, budget)
print(f"Nombre de combinaisons possibles : {len(all_combinations)}")
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
