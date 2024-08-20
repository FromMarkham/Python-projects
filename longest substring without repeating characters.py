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
        
    else:
        while i in string2:
            startvalue=startvalue+1 
            string2=string[startvalue:counter]            
            thelist.append(len(string2))
            
    
print(thelist)



#To see why this program ain't workin, see the list that is printed
#and compare the numbers you see on that list with where you are on
#the input string 

#For the sliding window algorithm to work, when the next character happens to
#be repeated again, you have to keep removing letters starting from the
#beginning of the string and keep doing that UNTIL that next character
#doesn't show up again. Your program just removes the character 1 time. 
