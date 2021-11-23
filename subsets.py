#Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

#using power set 
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