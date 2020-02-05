sp=[5,8,9,-32,87,0,66,-87,0,-95]
for i in range(len(sp)):
    if sp[i]<0:
        sp.insert(i,0)
        break
print(sp)
