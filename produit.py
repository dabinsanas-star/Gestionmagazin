#Saisie des  informations du produit*
ref = input("Donner la référence :")
designation = input("Donner la désignation :")
prix = float(input("Donner le prix unitaire :"))
#Affichage des informations
print("Référence :",ref)
print("Désignation :",designation)
print("Prix unitarire: ",prix,"DT")
# Saisie de la quantité
quantite = int(input("Donner la quantié en stock :"))
#Affichage de la quantité
print("Quantité en stock :")
#Calcul de la valeur du stock
valeur = prix*quantite
print("Valeur totale du stock :",valeur,"DT")