# Exercice 2 :  
# 1.Créer un tuple contenant des entiers et des chaînes. 
my_tuple = ("Aura",1,3,5,"Camilia",2,"Aura","Bostan")
print(my_tuple)
# 2. Tenter de modifier un élément et observer le message d’erreur. 
# 3. Construire un nouveau tuple issu du précédent mais : 
# o Sans doublons:
unique_tuple = tuple(set(my_tuple))
print(unique_tuple)
# o Trié selon la longueur des éléments (pour les chaînes):
    
# 4. Convertir ce tuple en liste, insérer un nouvel élément au milieu, puis reconvertir en 
# tuple.