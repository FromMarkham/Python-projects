

for t in range(11):
    if t==0:
        c=[1,1]
        z=[1,1]
        

    for i in range(0,len(c)-1): 
        ci=c[i]+c[i+1]
        z.insert(1,ci)
    c=z.copy()
    print(c)
    while len(z)>2:
        del z[1]


            




        

    



