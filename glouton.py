import time


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