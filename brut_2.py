
import time
"""
Ceux.py se contente de trier le dictipnnaire 
"""
# import open_csv

# csv_="/Users/davidravin/Desktop/Oρᥱᥒᥴᥣᥲssroom/Projet 7/data/datas_1.csv"
# open_csv(csv_)



actions =[
  {"name":"Action-1" ,"cost" : 20, "percent_benefit" : 5 },
  {"name":"Action-2" ,"cost" : 30, "percent_benefit" : 10 }, 
  {"name":"Action-3" ,"cost" : 50,"percent_benefit" : 15 },
  {"name":"Action-4" ,"cost" : 70,"percent_benefit" : 20 },
  {"name":"Action-5" ,"cost" : 60,"percent_benefit" : 17 },
  {"name":"Action-6" ,"cost" : 80,"percent_benefit" : 25 },
  {"name":"Action-7" ,"cost" : 22,"percent_benefit" : 7 },
  {"name":"Action-8" ,"cost" : 26,"percent_benefit" : 11 },
  {"name":"Action-9" ,"cost" : 48,"percent_benefit" : 13 },
  {"name":"Action-10" ,"cost" : 34,"percent_benefit" : 27 },
  {"name":"Action-11" ,"cost" : 42,"percent_benefit" : 17 },
  {"name":"Action-12" ,"cost" : 110, "percent_benefit" : 9 },
  {"name":"Action-13" ,"cost" : 38, "percent_benefit" : 23 },
  {"name":"Action-14" ,"cost" : 14,"percent_benefit" : 1 },
  {"name":"Action-15" ,"cost" : 18,"percent_benefit" : 3 },
  {"name":"Action-16" ,"cost" : 8,"percent_benefit" : 8 },
  {"name":"Action-17" ,"cost" : 4,"percent_benefit" : 12 },
  {"name":"Action-18" ,"cost" : 10,"percent_benefit" : 14 },
  {"name":"Action-19" ,"cost" : 24,"percent_benefit" : 21 },
  {"name":"Action-20" , "cost" : 114,"percent_benefit" : 18 }
    
]



"""
Calcile le cout de la fonction apres 2 ans 
"""

max_budget = 500

def formule_taux_benef(actions):
    results = []
    differences = [] 
    
    i = 1
    for action in actions:
        cost = action["cost"]
        benefit = action["percent_benefit"]
        value = round(cost * (1 + benefit / 100), 2)
        difference = round(value - cost,2)
        result = f"L'action-{i} avec un cout : {cost}, à une valeur de : {value}  avec un taux : {benefit}%, pour un interet de {difference} euro"
        
        results.append(result)
        differences.append(difference)
        i += 1
    return results, differences


def action_plus_chere_avec_budget(actions, max_budget):
    resultat_action_plus_chere_avec_budget = []
    resultats = formule_taux_benef(actions)
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
    resultats = formule_taux_benef(actions)
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




# def action_plus_benef(actions):
#     actions_triees = sorted(actions, key=lambda x: x["percent_benefit"], reverse=True)
#     resultat_action_plus_benef = []
    
#     for action in actions_triees:
#         #if action <= budget restant  append 
        
#         #if action 
#         resultat_action_plus_benef.append(f"L'action-{action['name']} a un bénéfice de {action['percent_benefit']}%")
#     return resultat_action_plus_benef



def action_plus_benef(actions, budget):
    start_time = time.time()  # Temps de début d'exécution
    
    # Triez les actions par bénéfice en pourcentage, en ordre décroissant
    actions_triees = sorted(actions, key=lambda x: x["percent_benefit"], reverse=True)
    
    # Liste pour stocker les actions que nous allons acheter
    resultat_action_plus_benef = []
    total_cost = 0

    for action in actions_triees:
        
        if total_cost + action["cost"] <= budget:
            # Ajoutez l'action à notre liste d'actions à acheter
            resultat_action_plus_benef.append(f"L'action-{action['name']} a un bénéfice de {action['percent_benefit']}%")
            
            # Ajoutez le coût de l'action au coût total
            total_cost += action["cost"]
    
    end_time = time.time()  # Temps de fin d'exécution
    execution_time = end_time - start_time  # Calcul du temps d'exécution
    
    print(f"Temps d'exécution : {execution_time:.6f} secondes")  # Affiche le temps d'exécution

    # Retournez les actions que nous avons décidé d'acheter
    return resultat_action_plus_benef







def action_moins_benef(actions):
    actions_triees = sorted(actions, key=lambda x: x["percent_benefit"])
    resultat_action_moins_benef = []
    for action in actions_triees:
        resultat_action_moins_benef.append(f"L'action-{action['name']} a un bénéfice de {action['percent_benefit']}%")
    return resultat_action_moins_benef



def calcul_rentabilite_action(prix_initial, taux_interet):
    percent_benefit = prix_initial * (1 + taux_interet) ** 2 - prix_initial
    return percent_benefit





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
actions_plus_benef = action_plus_benef(actions,max_budget)
for action in actions_plus_benef:
    print(action)

# Liste des actions avec les bénéfices les moins élevés
print("\nLa liste des actions avec les bénéfices les moins élevés :")
actions_moins_benef = action_moins_benef(actions)
for action in actions_moins_benef:
    print(action)
