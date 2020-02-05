sp=[5,8,9,-32,87,0,66,-87,0,-95]
k=0
for i in range(len(sp)):
    if sp[i]<0:
        k=k+1
print(k)
