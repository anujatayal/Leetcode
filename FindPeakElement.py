# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
# return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time. 

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

# Date- 13th July
# Approach- Use heap sort, store indexes and get index of 0th element

import heapq
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        numNegative=[-1*num for num in nums]
        heapq.heapify(numNegative)
        index=nums.index(-1*numNegative[0])
        return(index)  