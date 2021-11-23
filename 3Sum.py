# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        threeSum=set()
        for i in range(0,len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]==-nums[i]:
                    threeSum.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<-nums[i]:
                    j+=1
                else:
                    k-=1
        return list(threeSum)