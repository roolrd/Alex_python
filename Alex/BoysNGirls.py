N = float(input("Введіть кількість учнів у класі:" ))
M = float(input("Введіть кількість хлопців: " ))
pb = round(M / N * 100, 2)
pg = 100 - pb
print("В класі " + str(pb) + "% хлопців і " + str(pg) + "% дівчат")
