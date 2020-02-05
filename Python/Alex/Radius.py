import math
a = float(input("Введіть довжину сторони квадрата: "))
r = a / 2
R = round(a * math.sqrt(2) / 2, 3)
print("Радіус вписаного кола = " + str(r))
print("Радіус описаного кола = " + str(R))
