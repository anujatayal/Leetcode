# Given an integer array nums, return the number of triplets chosen from the array that can make triangles 
# if we take them as side lengths of a triangle.

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

#Naive Solution
#Time Limit Exceeded
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        if len(nums)<3:
            return count
        for firstside in range(len(nums)-2):
            for secondside in range(firstside+1,len(nums)-1):
                for thirdside in range(secondside+1,len(nums)):
                    if nums[firstside]+nums[secondside]>nums[thirdside] and nums[firstside]+nums[thirdside]>nums[secondside] and nums[thirdside]+nums[secondside]>nums[firstside]:
                        # print(nums[firstside],nums[secondside],nums[thirdside])
                        count+=1
        return count
                    