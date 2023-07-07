
"""
Ceux.py se contente de trier le dictipnnaire 
"""
from bruteforce import open_csv

csv_="/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/data/datas_1.csv"
open_csv(csv_)



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



"""
Calcile le cout de la fonction apres 2 ans 
"""

max_budget = 500

def formule(actions):
    results = []
    differences = [] 
    
    i = 1
    for action in actions:
        cost = action["cost"]
        benefit = action["benefice"]
        value = round(cost * (1 + benefit / 100), 2)
        difference = round(value - cost,2)
        result = f"L'action-{i} avec un cout : {cost}, à une valeur de : {value}  avec un taux : {benefit}%, pour un interet de {difference} euro"
        
        results.append(result)
        differences.append(difference)
        i += 1
    return results, differences


def action_plus_chere_avec_budget(actions, max_budget):
    resultat_action_plus_chere_avec_budget = []
    resultats = formule(actions)
    actions_triees = sorted(resultats[0], key=lambda x: float(x.split("valeur de : ")[1].split(" ")[0]), reverse=True)

    total_budget = 0

    for resultat in actions_triees:
        valeur_action = float(resultat.split("valeur de : ")[1].split(" ")[0])
        if total_budget + valeur_action <= max_budget:
            resultat_formate = resultat.ljust(30)
            resultat_action_plus_chere_avec_budget.append(resultat_formate)
            total_budget += valeur_action
        else:
            break

    return resultat_action_plus_chere_avec_budget


def action_moins_chere_avec_budget(actions, max_budget):
    resultat_action_moins_chere = []
    resultats = formule(actions)
    actions_triees = sorted(resultats[0], key=lambda x: float(x.split("valeur de : ")[1].split(" ")[0]), reverse=True)

    total_budget = 0

    for resultat in actions_triees:
        valeur_action = float(resultat.split("valeur de : ")[1].split(" ")[0])
        if total_budget + valeur_action <= max_budget:
            resultat_formate = resultat.ljust(50)
            resultat_action_moins_chere.append(resultat_formate)
            total_budget += valeur_action
        else:
            break
    
    return resultat_action_moins_chere




def action_plus_benef(actions):
    actions_triees = sorted(actions, key=lambda x: x["benefice"], reverse=True)
    resultat_action_plus_benef = []
    for action in actions_triees:
        resultat_action_plus_benef.append(f"L'action-{action['name']} a un bénéfice de {action['benefice']}%")
    return resultat_action_plus_benef


def action_moins_benef(actions):
    actions_triees = sorted(actions, key=lambda x: x["benefice"])
    resultat_action_moins_benef = []
    for action in actions_triees:
        resultat_action_moins_benef.append(f"L'action-{action['name']} a un bénéfice de {action['benefice']}%")
    return resultat_action_moins_benef



def calcul_rentabilite_action(prix_initial, taux_interet):
    benefice = prix_initial * (1 + taux_interet) ** 2 - prix_initial
    return benefice





# Liste des actions les plus chères en fonction du budget
print(f"La liste des actions les plus chères pour un budget de {max_budget} euros :")
actions_plus_cheres = action_plus_chere_avec_budget(actions, max_budget)
for action in actions_plus_cheres:
    print(action)

print("\nNombre d'actions  chères :", len(actions_plus_cheres))

# Liste des actions les moins chères en fonction du budget
print(f"\nLa liste des actions les moins chères pour un budget de {max_budget} euros :")
actions_moins_cheres = action_moins_chere_avec_budget(actions, max_budget)
for action in actions_moins_cheres:
    print(action)

print("\nNombre d'actions pas chères :", len(actions_moins_cheres))

# Liste des actions avec les bénéfices les plus élevés
print("\nLa liste des actions avec les bénéfices les plus élevés :")
actions_plus_benef = action_plus_benef(actions)
for action in actions_plus_benef:
    print(action)

# Liste des actions avec les bénéfices les moins élevés
print("\nLa liste des actions avec les bénéfices les moins élevés :")
actions_moins_benef = action_moins_benef(actions)
for action in actions_moins_benef:
    print(action)
