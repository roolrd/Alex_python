while True:
    print("Зробіть вибір")
    print("Введіть 'e' щоб почати розрахунок")
    print("Введіть 'q' щоб закінчити програму")
    print("Введіть 'g' щоб знайти решту")
    choice=input(": ")
    if choice == "q":
        break
    elif choice == "e":
        t = float(input("Введи масу тортика: "))
        p = float(input("Введи масу порції будь-ласка: "))
        gost = str(t // p)
    elif choice == "g":
        t = float(input("Введи масу тортика: "))
        p = float(input("Введи масу порції будь-ласка: "))
        gost = str(t % p)
    else:
        print("Unnown input")
    print("ВІдпоіДь: " + gost)
