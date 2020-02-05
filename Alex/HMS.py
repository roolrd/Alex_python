timeS = int(input("Введіть час в секундах: "))
hour = timeS // 3600
min = (timeS % 3600) // 60
sec = (timeS % 3600) % 60
print(str(hour) + " годин(a) " + str(min) + " хвилин(a) " + str(sec) + " секунд")
