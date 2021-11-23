# Given an integer array nums, find the contiguous subarray (containing at least one number) which has 
# the largest sum and return its sum.
# # A subarray is a contiguous part of an array.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxFar=-inf
        maxhere=0
        for i in nums:
            maxhere=maxhere+i
            if maxFar<maxhere:
                maxFar=maxhere
            if maxhere<0:
                maxhere=0
        return maxFar
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax=nums[0]
        maxFar=nums[0]
        startIndex=0
        endIndex=0
        for i in range(1,len(nums)):
            curMax=max(nums[i],curMax+nums[i])
            maxFar=max(curMax,maxFar)
            if maxFar==curMax and curMax==nums[i]:
                startIndex=i
                endIndex=i
            elif maxFar==curMax and curMax!=nums[i]:
                endIndex=i+1
        print(nums[startIndex:endIndex])
        return maxFar