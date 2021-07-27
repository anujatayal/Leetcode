#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.
#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn=set(nums) #to remove duplicate nos
        lces=0 #empty set   
        for no in setn: #iterate over set
            count=1
            if no-1 not in setn: #ignore intermediate nos, start with smaller no
                while no+1 in setn: #go till max no in sequence
                    count+=1
                    no=no+1
            #print(no,count)
            if count>lces: #store longest sequence
                lces=count
        return (lces)