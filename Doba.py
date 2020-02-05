d=int(input('Введіть годину'))
if d>5 and d<12:
    print('Ранок')
elif d>11 and d<19:
    print('День')
elif d>19 and d<24:
    print('Вечір')
elif d>0 and d<6:
    print('Ніч')
