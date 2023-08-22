import csv
from optimized import optimized

budget = 500

def charger_donnees(fichier):
    actions = []
    with open(fichier, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            actions.append({
                'name': row['name'],
                'cost': int(float(row['price']) * 100),  # Multiplie par 100 pour convertir en centimes
                'percent_benefit': (float(row['profit']) - float(row['price'])) / float(row['price']) * 100 if float(row['price']) != 0 else 0
            })
    return actions

donnees_2 = charger_donnees("/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/data/datas_2.csv")
donnees_1 = charger_donnees("/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/data/datas_1.csv")

# Pour données_2
meilleure_combinaison2, max_benefit2 = optimized(donnees_2, budget)
print("Actions suggérées par optimized pour le fichier datas_2 :")
for action in meilleure_combinaison2:
    print(action['name'])
print(f"Bénéfice maximal suggéré par optimized pour le fichier datas_2 : {max_benefit2:.2f}€")

print("\nActions achetées par Sienna dans datas_2 :")
actions_achetees_sienna_2 = [
    "Share-ECAQ",
"Share-IXCI",
"Share-FWBE",
"Share-ZOFA",
"Share-PLLK",
"Share-YFVZ",
"Share-ANFX",
"Share-PATS",
"Share-NDKR",
"Share-ALIY",
"Share-JWGF",
"Share-JGTW",
"Share-FAPS",
"Share-VCAX",
"Share-LFXB",
"Share-DWSK",
"Share-XQII",
"Share-ROOM"
]
for action in actions_achetees_sienna_2:
    print(action)
    
print("\n-------------------------\n")

# Pour données_1
meilleure_combinaison1, max_benefit1 = optimized(donnees_1, budget)
print("Actions suggérées par l'algorithme pour le fichier datas_1 :")
for action in meilleure_combinaison1:
    print(action['name'])
print(f"Bénéfice maximal suggéré par l'algorithme pour le fichier datas_1 : {max_benefit1:.2f}€")

print("\nActions achetées par Sienna dans datas_1 :")
actions_achetees_sienna_1 = [
    "Share-GRUT"
]
for action in actions_achetees_sienna_1:
    print(action)
