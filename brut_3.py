def calcul_rentabilite_action(prix_initial, taux_interet):
    percent_benefit = prix_initial * (1 + taux_interet) ** 2 - prix_initial
    return percent_benefit


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

for action in actions:
    prix_initial = action["cost"]
    taux_interet = action["percent_benefit"] / 100
    rentabilite = calcul_rentabilite_action(prix_initial, taux_interet)
    print("Rentabilité de", action["name"], ":", rentabilite)
