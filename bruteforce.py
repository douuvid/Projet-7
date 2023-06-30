# #1) commencer par la formule cout + interet

# def formule___(cout: int, benef: float):
#     i = 1
#     benef = 1 + benef / 100  # Convert the percentage benefit to a decimal value
#     result = cout * benef

#     return f"L'action-{i} vaut : {result}"

# print(formule___(20, 5))

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
max_budget = 500


"""
Calcile le cout de la fonction apres 2 ans 
"""
def formule(actions):
    results = []
    i = 1
    for action in actions:
        cost = action["cost"]
        benefit = action["benefice"]
        value = round(cost * (1 + benefit / 100), 2)
        result = f"L'action-{i} vaut : {value} avec un taux de {benefit}% apres deux ans"
        results.append(result)
        i += 1
        
    return results


results = formule(actions)
sorted_results = sorted(results, key=lambda x: float(x.split("vaut : ")[1].split(" ")[0]), reverse=True)

# for result in sorted_results:
#     print(result)

###Methode avec les action les plus chere 


        
def action_plus_chere(actions, max_budget):
    resultat_action_plus_chere = []
    resultats = formule(actions)
    actions_triees = sorted(resultats, key=lambda x: float(x.split("vaut : ")[1].split(" ")[0]), reverse=True)
    total_budget = 0

    for resultat in actions_triees:
        valeur_action = float(resultat.split("vaut : ")[1].split(" ")[0])
        if total_budget + valeur_action <= max_budget:
            resultat_formate = resultat.ljust(50)
            resultat_action_plus_chere.append(resultat_formate)
            total_budget += valeur_action
        else:
            break

    return resultat_action_plus_chere

print(f"La liste des actions les plus chere en fonction du budget de :  {max_budget} euro")
print("")

print(action_plus_chere(actions, max_budget))

action_cher=len(action_plus_chere(actions, max_budget))
print("Nombre d'actions pas chères : ", action_cher)



###Methode avec les action les moins chere 
def action_moins_chere(actions, max_budget):
    resultat_action_moins_chere = []
    
    resultats = formule(actions)
    actions_triees = sorted(resultats, key=lambda x: float(x.split("vaut : ")[1].split(" ")[0]))
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

# print(f"La liste des actions les moins chere en fonction du budget de :  {max_budget} euro")
# print("")

# print(action_moins_chere(actions, max_budget))

# x=len(action_moins_chere(actions, max_budget))
# print("Nombre d'actions pas chères : ", x)




###Methode avec les benef les plus eleve

###Methode avec les action les moins  eleve  


    
