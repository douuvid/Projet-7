def optimized(actions, budget):
    nombre_actions = len(actions)  # On compte le nombre total d'actions

    # On initialise un tableau pour stocker nos calculs intermédiaires.
    # Le tableau a (nombre_actions + 1) lignes et (budget + 1) colonnes.
    # On remplit le tableau avec des zéros.
    tableau = []
    for _ in range(nombre_actions + 1):
        tableau.append([0] * (budget + 1))

    # On parcourt le tableau ligne par ligne
    for i in range(1, nombre_actions + 1):
        for c in range(1, budget + 1):
            # Le coût de l'action actuelle est le coût de l'action à l'index (i - 1) dans la liste des actions
            cout_action_actuelle = actions[i - 1]["cost"]

            # Le bénéfice de l'action actuelle est le pourcentage de bénéfice de l'action à l'index (i - 1) dans la liste des actions,
            # multiplié par le coût de cette action
            benefice_action_actuelle = actions[i - 1]["cost"] * actions[i - 1]["percent_benefit"] / 100

            # Si le coût de l'action actuelle est inférieur ou égal à la capacité actuelle du sac à dos (c)
            if cout_action_actuelle <= c:
                # On peut choisir d'inclure l'action actuelle dans le sac à dos.
                # Si on l'inclut, le bénéfice total est le bénéfice de l'action actuelle, plus le bénéfice total qu'on peut obtenir
                # avec le reste de la capacité du sac à dos (c - cout_action_actuelle).
                # Si on n'inclut pas l'action actuelle, le bénéfice total est le même que le bénéfice total de la ligne précédente.
                tableau[i][c] = max(tableau[i - 1][c], tableau[i - 1][c - cout_action_actuelle] + benefice_action_actuelle)
            else:
                # Si le coût de l'action actuelle est supérieur à la capacité actuelle du sac à dos, on ne peut pas inclure l'action actuelle.
                # Donc, le bénéfice total est le même que le bénéfice total de la ligne précédente.
                tableau[i][c] = tableau[i - 1][c]

    # Maintenant, on retrouve la meilleure combinaison d'actions.
    meilleure_combinaison = []
    c = budget
    for i in range(nombre_actions, 0, -1):
        # Si le bénéfice total de la ligne actuelle est différent du bénéfice total de la ligne précédente,
        # cela signifie que l'action à l'index (i - 1) dans la liste des actions a été incluse dans la meilleure combinaison.
        if tableau[i][c] != tableau[i - 1][c]:
            meilleure_combinaison.append(actions[i - 1])
            c -= actions[i - 1]["cost"]

    return meilleure_combinaison, tableau[nombre_actions][budget]