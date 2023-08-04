# #1) commencer par la formule cout + interet

# def formule___(cout: int, benef: float):
#     i = 1
#     benef = 1 + benef / 100  # Convert the percentage benefit to a decimal value
#     result = cout * benef

#     return f"L'action-{i} vaut : {result}"

# print(formule___(20, 5))

import csv


def open_csv(csv_path):
    with open(csv_path, 'r') as fichier:
        lecteur_csv = csv.reader(fichier)
        result = []
        next(lecteur_csv)  # Saute la première ligne (en-têtes)
        for action in lecteur_csv:
            name = action[0]
            cost = float(action[1])
            print(f"{name} : {cost}")
            result.append((name, cost))
        print("Fichier 1 : datas_1")
        return result


csv_ = ["datas_1", "datas_2"]
resultats = []

for csv_name in csv_:
    print(f"Lecture du fichier : {csv_name}")
    csv_path = f"/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/data/{csv_name}.csv"

    result = open_csv(csv_path)
    resultats.append((csv_name, result))


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
max_budget = 500


"""
Calcile le cout de la fonction apres 2 ans 
"""


def formule(actions):
    results = []
    i = 1
    for action in actions:
        cost = action["cost"]
        benefit = action["percent_benefit"]
        value = round(cost * (1 + benefit / 100), 2)
        result = f"L'action-{i} vaut : {value} avec un taux de {benefit}%"
        results.append(result)
        i += 1

    return results


results = formule(actions)
sorted_results = sorted(results, key=lambda x: float(
    x.split("vaut : ")[1].split(" ")[0]), reverse=True)

# for result in sorted_results:
#     print(result)

# Methode avec les action les plus chere


def action_plus_chere_avec_budget(actions, max_budget):
    resultat_action_plus_chere_avec_budget = []
    resultats = formule(actions)
    actions_triees = sorted(resultats, key=lambda x: float(
        x.split("vaut : ")[1].split(" ")[0]), reverse=True)
    total_budget = 0

    for resultat in actions_triees:
        valeur_action = float(resultat.split("vaut : ")[1].split(" ")[0])
        if total_budget + valeur_action <= max_budget:
            resultat_formate = resultat.ljust(30)
            resultat_action_plus_chere_avec_budget.append(resultat_formate)
            total_budget += valeur_action
        else:
            break

    return resultat_action_plus_chere_avec_budget


print(
    f"La liste des actions les plus chere en fonction du budget de :  {max_budget} euro")
print("")

print(action_plus_chere_avec_budget(actions, max_budget))

action_cher = len(action_plus_chere_avec_budget(actions, max_budget))
print("Nombre d'actions pas chères : ", action_cher)


# Methode avec les action les moins chere
def action_moins_chere(actions, max_budget):
    resultat_action_moins_chere = []

    resultats = formule(actions)
    actions_triees = sorted(resultats, key=lambda x: float(
        x.split("vaut : ")[1].split(" ")[0]))
    total_budget = 0

    for resultat in actions_triees:
        valeur_action = float(resultat.split("vaut : ")[1].split(" ")[0])
        if total_budget + valeur_action <= max_budget:
            resultat_formate = resultat.ljust(50)
            resultat_action_moins_chere.append(resultat_formate)
            total_budget += valeur_action
        else:
            break

    return resultat_action_moins_chere


print(
    f"La liste des actions les moins chere en fonction du budget de :  {max_budget} euro")
print("")

action_moins_chere(actions, max_budget)

x = len(action_moins_chere(actions, max_budget))
print("Nombre d'actions pas chères : ", x)


# Methode avec les benef les plus eleve
# Trier le taux
actions_sorted = sorted(
    actions, key=lambda x: x["percent_benefit"], reverse=True)
# Methode avec les action les moins  eleve
