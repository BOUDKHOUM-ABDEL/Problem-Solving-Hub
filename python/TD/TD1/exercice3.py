# Exercice 3 : 
# �crire un programme qui : 
# 1. Lit une phrase saisie par l�utilisateur:
phrase = input("Enter a sentences : ")


# 2. Affiche : 
# o Nombre de mots:
#-----------------------------------------------------
#mots = phrase.split()  # S�pare la phrase en mots
#nbr_word = len(mots)   # Compte le nombre de mots
#-----------------------------------------------------
nbr_word=1
for char in phrase :
    if char==" ":
        nbr_word +=1
print(nbr_word)

# o Mot le plus long et le plus court:
words = phrase.split()# S�pare la phrase en mots



           # Parcourir les mots pour trouver le plus long et le plus court
max_len = len(words[0])
min_len = len(words[0])

for w in words:
    if len(w) > max_len:
        max_len = len(w)
    if len(w) < min_len:
        min_len = len(w)

           # Collecter tous les mots qui ont cette longueur
longest_words = []
shortest_words = []

for w in words:
    if len(w) == max_len:
        longest_words.append(w)
    if len(w) == min_len:
        shortest_words.append(w)

print("Mots les plus longs :", longest_words)
print("Mots les plus courts :", shortest_words)


# o Fr�quence de chaque lettre (sans collections.Counter): 
# o Phrase invers�e mot par mot (sans split() invers� directement). 
# 3. V�rifie si la phrase est un pangramme (contient toutes les lettres de l�alphabet).