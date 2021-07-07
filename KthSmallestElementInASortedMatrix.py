# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# 7th July 2021
class Solution:
    def sortList(self,l1,l2):
        l3=[]
        i1=0
        i2=0
        while i1<len(l1) and i2<len(l2):
            if l1[i1]<l2[i2]:
                l3.append(l1[i1])
                i1+=1
            else:
                l3.append(l2[i2])
                i2+=1
        if i1==len(l1):
            l3.extend(l2[i2:])
        else:
            l3.extend(l1[i1:])
        return(l3)
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sortedList=matrix[0]
        for rowNo in range(1,len(matrix)):
            sortedList=self.sortList(matrix[rowNo],sortedList)
        return(sortedList[k-1])
        

