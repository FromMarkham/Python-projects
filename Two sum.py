class Solution(object):
    def twoSum(self,nums,target):
        for a in range(len(nums)):
            Numstarget=target-nums[a]
            for b in range(len(nums)):
                if Numstarget==nums[b]:
                    IndiceList=[a,b]
        return IndiceList
