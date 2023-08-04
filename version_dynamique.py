from itertools import combinations
import csv
import logging
import time


def taux_de_rendement(prix_achat, prix_vente):
    logging.info('Début du calcul du rendement.')

    if prix_achat is not None and prix_vente is not None:
        logging.debug('Les prix d\'achat et de vente sont fournis.')

        prix_achat_float = float(prix_achat.replace(',', '.')) 
        prix_vente_float = float(prix_vente.replace(',', '.')) 

        logging.info(f'Prix d\'achat converti en float: {prix_achat_float}, Prix de vente converti en float: {prix_vente_float}')

        if prix_achat_float > 0:
            rendement = ((prix_vente_float - prix_achat_float) / prix_achat_float) * 100

            logging.debug(f'Rendement calculé: {rendement}')

            if rendement >= 0:
                logging.debug('Rendement positif.')
                return f"Bon rendement chacal : {round(rendement)}🔥⬆️"
            else:
                logging.debug('Rendement négatif.')
                return f"Vous avez subi une perte de {abs(rendement):.2f}% 🥶⬇️"
        else:
            logging.warning('Rendement impossible à calculer (prix d\'achat nul)')
            return "Rendement impossible à calculer (prix d'achat nul)"
    else:
        logging.warning('Rendement impossible à calculer (fichier corrompus)')
        return "Rendement impossible à calculer (fichier corrompus)"

    
    ##24 juillet 
  


    

def calculer_taux_de_rendement_fichier_csv(nom_fichier):
    with open(nom_fichier, newline='') as csvfile:
        # Spécifier manuellement les noms des colonnes avec fieldnames
        fieldnames = ['name', 'price', 'profit']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        # Ignorer la première ligne (en-tête) car nous l'avons spécifiée manuellement
        next(reader)
        total_achat_action = 0
        somme_total_action = 0  # Initialiser la somme totale à zéro

        for row in reader:
            nom_action = row['name']
            prix_achat = row["price"]
            prix_vente = row["profit"]
            
            if prix_achat != "0":
                resultat = taux_de_rendement(prix_achat, prix_vente)
                logging.debug(f"Action : {nom_action}, Taux de rendement : {resultat}%")
            else:
                logging.warning(f"L'action {nom_action} a un prix d'achat de 0. Son taux de rendement n'est pas calculé.")
            total_achat_action += 1
            
            try:
                somme_total_action += float(prix_achat.replace(',', '.'))  # Ajouter le prix d'achat à la somme totale
            except ValueError:
                logging.warning(f"Erreur : Impossible de convertir le prix d'achat de l'action {nom_action} en float.")
                continue

        logging.info(f"Le nombre total d'actions est : {total_achat_action} action pour un montant total de {somme_total_action:.2f} euro")
        # print(f"Pour le fichier {name_file}")




"""

    Conclusion

    Avec un calcule de une formule de taux de rendement 
    On peut voir des erreurs 
    Notamment qu'il y a des case nul qui on fait du profit wtf
    + taux rendement negatif
"""