def optimized(actions, budget):
    # Convertissons le budget en centimes
    budget = int(budget * 100)

    nombre_actions = len(actions)  # On compte le nombre total d'actions

    # Initialisation du tableau pour stocker nos calculs intermédiaires.
    tableau = [[0] * (budget + 1) for _ in range(nombre_actions + 1)]

    # Parcours du tableau ligne par ligne
    for i in range(1, nombre_actions + 1):
        for c in range(1, budget + 1):
            # Le coût de l'action actuelle converti en centimes
            cout_action_actuelle = int(actions[i - 1]["cost"] * 100)

            # Le bénéfice de l'action actuelle converti en centimes
            benefice_action_actuelle = int(actions[i - 1]["cost"] * actions[i - 1]["percent_benefit"])

            # Si le coût de l'action actuelle est inférieur ou égal à la capacité actuelle du sac à dos (c)
            if cout_action_actuelle <= c:
                # On ajoute une vérification pour éviter l'erreur d'index
                if 0 <= c - cout_action_actuelle < len(tableau[i - 1]):
                    tableau[i][c] = max(tableau[i - 1][c], tableau[i - 1][c - cout_action_actuelle] + benefice_action_actuelle)
                else:
                    tableau[i][c] = tableau[i - 1][c]
            else:
                tableau[i][c] = tableau[i - 1][c]

    # Retrouvons la meilleure combinaison d'actions.
    meilleure_combinaison = []
    c = budget
    for i in range(nombre_actions, 0, -1):
        if tableau[i][c] != tableau[i - 1][c]:
            meilleure_combinaison.append(actions[i - 1])
            c -= int(actions[i - 1]["cost"] * 100)

    # Convertissons le bénéfice total de retour à des euros depuis des centimes
    return meilleure_combinaison, tableau[nombre_actions][budget] / 100

