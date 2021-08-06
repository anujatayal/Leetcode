import math
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # length(nums)
        subsetLength=int(math.pow(2,len(nums)))
        print(subsetLength)
        for counter in range(0,subsetLength):
            for j in range(0,len(nums)):
                # print(j,counter,1<<j,(counter & (1<<j)))
                if((counter & (1<<j))>0):
                    print(nums[j],end="")
            print()