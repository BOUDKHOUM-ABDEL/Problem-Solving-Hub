
print("This program solves a second degree equation of the form ax^2 + bx + c = 0")

a=float(input("Enter a (a != 0): "))
while a == 0:
    a=float(input("a must be different from 0. Enter a (a != 0): "))

b=float(input("Enter b: "))
c=float(input("Enter c: "))

D=b**2-4*a*c
if D < 0:
    print("The equation has no real solution.")
elif D == 0:
    x=-b/(2*a)
    print(f"The equation has one real solution: x = {x : .2f}")
else:
    x1=(-b - D**0.5)/(2*a) # racine carree de D
    x2=(-b + D**0.5)/(2*a) # racine carree de D
    print(f"The equation has two real solutions: x1 = {x1 : .2f} and x2 = {x2 : .2f}")

