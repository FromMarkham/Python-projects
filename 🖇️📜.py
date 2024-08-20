thelist=[]


class mylinkedlist:
    def __init__(self, value, nextnode=None):
        self.value=value
        self.nextnode=nextnode 



number1=mylinkedlist(1)
number2=mylinkedlist(4)
number3=mylinkedlist(27)

number1.nextnode=number2
number2.nextnode=number3

currentnode=number1 

while True:
    thelist.append((currentnode.value))
    if currentnode.nextnode==None:
        break
    currentnode=currentnode.nextnode

print(thelist)



#number1.nextNode=number2
#number2.nextNode=number1

