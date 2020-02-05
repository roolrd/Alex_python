list=[0,2,4,6,8,10]
k=0
for i in range(len(list)):
    if list[i]==2*i:
        k=list[i]+k
print(k)
