
# Écrire un programme qui : 
# 1. Crée une liste de nombres entiers saisis par l’utilisateur. 

my_list = []
lenth = 5
for index in range(lenth):
    number = int(input(f"Enter the {index+1}th number : "))
    my_list.append(number)
print(my_list)
    
# 2. Affiche : 
# o Liste triée sans utiliser sort() ni sorted():
for i in range(lenth):
    for j in range(i+1,lenth):
        if my_list[i] > my_list[j]:
            temp = my_list[j]
            my_list[j] = my_list[i]
            my_list[i] = temp
print(my_list)
    
# o Deuxième plus grand élément:
index =lenth -1
if my_list[0] == my_list[index]:
    print("not found, all numbers are simillar")

else:
   while my_list[index] == my_list[index-1]:
    index=index-1
   print(my_list[index-1])

# o Somme des éléments aux indices pairs, 
# o Nouvelle liste contenant uniquement les valeurs uniques (sans utiliser set()). 
# 3. Remplace dans la liste tous les éléments négatifs par 0. 