nums=[4,1,2,0,8]
Target=12
Numstarget=0
IndiceList=[]
IndiceList2=[]


for a in range(len(nums)):
    Numstarget=Target-nums[a]
    for b in range(len(nums)):
        if Numstarget==nums[b]:
            IndiceList=[a,b]
print(IndiceList)

                
        
        
        
