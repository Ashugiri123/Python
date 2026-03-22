import math

radius = float(input("enter the radius in cm:"))
circumference = 2 * math.pi * radius
print(f"the circumference is: {round(circumference,2)}cm")
area = 2 * math.pi * pow(radius,2)
print(f"area:{round(area,2)} cm^2")

# code for triangle
a = float(input("enter the side a :"))
b = float(input("enter the side b:"))
c=  math.sqrt(pow(a,2)+ pow(b,2))
print(f"side of triange is {round(c,2)}")