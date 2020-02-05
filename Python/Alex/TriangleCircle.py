import math
a = float(input("Введіть довжину першого катета(см): "))
b = float(input("Введіть довжину другого катета(см): "))
c = math.sqrt(a**2 + b**2)
area = math.pi*(c / 2)**2 
print("Площа круга = " + str(area) + " см.кв.")
