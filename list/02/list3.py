list=[1,5,4,9,7,2]
k=1
for i in range(len(list)):
    if list[i]>(list[len(list)-1]):
        k=list[i]*k
print(k)

