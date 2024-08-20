list1=[]
list2=[]

class mylinkedlist:
    def __init__(self, value, nextnode=None):
        self.value=value
        self.nextnode=nextnode 

number1=mylinkedlist('1')
number2=mylinkedlist('4')
number3=mylinkedlist('2')
#problem here is is that if 1 half of the linked list is of a different length
#then the other. This means that the code will keep running for the longer side, and appending none to one of the lists 
number4=mylinkedlist('2') 
number5=mylinkedlist('3')
number6=mylinkedlist('4')
number7=mylinkedlist('5')

number1.nextnode=number2
number2.nextnode=number3

number4.nextnode=number5
number5.nextnode=number6
number6.nextnode=number7

currentnode=number1

currentnode2=number4 

while True:
    list1.append((currentnode.value))
    list2.append((currentnode2.value))
    
    if currentnode.nextnode==None and currentnode2.nextnode==None:
        break
    currentnode=currentnode.nextnode
    currentnode2=currentnode2.nextnode 

print(list1)
print(list2)

#-----------------------------------------------------------------------
c="T"

list1.reverse()
list2.reverse()

list1b=c.join(list1)
list2b=c.join(list2)

list1c=list1b.replace("T","")
list2c=list2b.replace("T","")

list1d=int(list1c)
list2d=int(list2c)

list3c=list1d+list2d

print(list3c)


