# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
#  You may assume that the majority element always exists in the array.class Solution:
def majorityElement(self, nums: List[int]) -> int:
    if len(nums)==0:
        return 
    if len(nums)==1:
        return nums[0]
    else:
        mid=int(len(nums)/2)
        leftM=self.majorityElement(nums[0:mid]) 
        rightM=self.majorityElement(nums[mid:]) 
        if leftM==rightM:
            return leftM
        else:
            countL=nums.count(leftM)
            countR=nums.count(rightM)
            if countL>len(nums)/2:
                return leftM
            else:
                return rightM