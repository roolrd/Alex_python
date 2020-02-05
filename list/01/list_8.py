sp=[5,8,9,32,87,25,66,0,37,95]
sp2=[]
for i in range(len(sp)):
    if sp[i]%2!=0:
        sp2.append(sp[i])
sp=sp2
print (sp)
