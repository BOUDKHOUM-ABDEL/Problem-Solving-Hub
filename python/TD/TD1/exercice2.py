# Exercice 2 :  
# 1.Cr�er un tuple contenant des entiers et des cha�nes. 
my_tuple = ("Aura",1,3,5,"Camilia",2,"Aura","Bostan")
print(my_tuple)
# 2. Tenter de modifier un �l�ment et observer le message d�erreur. 
# 3. Construire un nouveau tuple issu du pr�c�dent mais : 
# o Sans doublons:
unique_tuple = tuple(set(my_tuple))
print(unique_tuple)
# o Tri� selon la longueur des �l�ments (pour les cha�nes):
    
# 4. Convertir ce tuple en liste, ins�rer un nouvel �l�ment au milieu, puis reconvertir en 
# tuple.