# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c 
# keeping its original data. You are given an m x n matrix mat and two integers r and c representing the row number and column number 
# of the wanted reshaped matrix. The reshaped matrix should be filled with all the elements of the original matrix in the same 
# row-traversing order as they were. If the reshape operation with given parameters is possible and legal, output the new reshaped 
# matrix; Otherwise, output the original matrix.
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# 6th July 2021

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        else:
            j=0
            emptyList=[]
            matOutput=[]
            for row,rowValues in enumerate(mat):
                for colvalues in rowValues:
                    if j<c:
                        j+=1
                        emptyList.append(colvalues)
                    else:
                        j=1
                        matOutput.append(emptyList)
                        emptyList=[]
                        emptyList.append(colvalues)
            matOutput.append(emptyList)
            return(matOutput)