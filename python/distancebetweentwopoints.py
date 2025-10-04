
import math

x1=float(input("Enter xA: "))
y1=float(input("Enter yA: "))
x2=float(input("Enter xB: "))
y2=float(input("Enter yB: "))

D=math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"Distance between A and B is: { D : .2f} cm")