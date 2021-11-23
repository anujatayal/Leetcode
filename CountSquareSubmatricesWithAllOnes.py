# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for rows in range(len(matrix)):
            for j in range(len(matrix[rows])):
                # print(matrix[rows][j])
                if rows==0 or j==0:
                    matrix[rows][j]=matrix[rows][j]
                elif matrix[rows][j]!=0:
                    matrix[rows][j]=min(matrix[rows-1][j],matrix[rows][j-1],matrix[rows-1][j-1])+1
        count=0
        for rows in matrix:
            # print(rows)
            count+=sum(rows)
        return(count)
        