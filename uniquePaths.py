# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#Case1: Recursion
#Time Limit Exceeded

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        elif m==0 or n==0:
            return 0
        else:
            return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

# memoization

class Solution:
    def memoization(self,memo,m:int,n:int)->int:
        if m==0 or n==0:
            return 0
        elif str(m)+","+str(n) in memo:
            return memo[str(m)+","+str(n)]
        else:
            memo[str(m)+","+str(n)]=self.memoization(memo,m-1,n)+self.memoization(memo,m,n-1)
            return memo[str(m)+","+str(n)]
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        memo["1,1"]=1
        return self.memoization(memo,m,n)
        