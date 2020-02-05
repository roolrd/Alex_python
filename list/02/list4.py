list=[5,7,9,-8,96,-78,6,-98,-5,4,67,9,5,78,68,85]
for i in range(len(list)):
    if list[i]<0:
        list[i]=list[i]**2
print(list)
