
thelist=[]
thelist2=[]
string="iuefhiuhweqf"
string2=""
startvalue=0
counter=0

for i in string:
    if i not in string2:
        counter=counter+1        
        string2=string[startvalue:counter]
        thelist.append(len(string2))

print(string2)
