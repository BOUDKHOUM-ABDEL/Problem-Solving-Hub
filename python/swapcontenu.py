
#swap contenu.py    
# Permet de swapper le contenu de deux variables
#technique 1
a = 5
b = 10
print("Avant le swap : a =", a, ", b =", b)
a, b = b, a
print("Apres le swap : a =", a, ", b =", b)

#technique 2 avec une variable temporaire
a = 5
b = 10
print("Avant le swap : a =", a, ", b =", b)
temp = a
a = b
b = temp
print("Apres le swap : a =", a, ", b =", b)
#technique 3 avec les operations mathematiques
a = 5
b = 10
print("Avant le swap : a =", a, ", b =", b)
a = a + b  # a devient 15
b = a - b  # b devient 5
a = a - b  # a devient 10
print("Apres le swap : a =", a, ", b =", b)