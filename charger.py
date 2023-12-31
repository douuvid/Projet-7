import csv
from optimized import optimized
from brut import formule,action_plus_chere_avec_budget


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
 
 
#Pour la logique de S

# resultat=formule(donnees_1)
# for r in resultat:
#     print(r)
    
# actions_plus_cheres_sienna = action_plus_chere_avec_budget(donnees_1, budget)
# print("\nActions les plus chères avec le budget selon notre méthode :")
# for action in actions_plus_cheres_sienna:
#     print(action)







# def actions_sienna(actions, liste_sienna_names):
#     return [action for action in actions if action['name'] in liste_sienna_names]
# def calcul_valeur_sienna(actions, liste_sienna_names):
#     actions_sienna = [
#         action for action in actions if action['name'] in liste_sienna_names]
#     return formule(actions_sienna)


# # Liste des noms des actions de Sienna
# noms_sienna = ["Share-ECAQ",
#                "Share-IXCI",
#                "Share-FWBE",
#                "Share-ZOFA",
#                "Share-PLLK",
#                "Share-YFVZ",
#                "Share-ANFX",
#                "Share-PATS",
#                "Share-NDKR",
#                "Share-ALIY",
#                "Share-JWGF",
#                "Share-JGTW",
#                "Share-FAPS",
#                "Share-VCAX",
#                "Share-LFXB",
#                "Share-DWSK",
#                "Share-XQII",
#                "Share-ROOM"]  

# actions_choisies = actions_sienna(donnees_2, noms_sienna)

# # Calculer et trier par rendement
# actions_triees_par_rendement = sorted(actions_choisies, key=lambda x: x['percent_benefit'], reverse=True)

# # Afficher les résultats
# print("Actions choisies par Sienna, triées par rendement :")
# for action in actions_triees_par_rendement:
#     print(f"{action['name']} - Rendement: {action['percent_benefit']:.2f}%")
